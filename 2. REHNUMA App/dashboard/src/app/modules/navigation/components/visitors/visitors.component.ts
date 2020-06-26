import { Component, Directive, ViewChildren, QueryList, Input, Output, PipeTransform } from '@angular/core';
import { CdkDragDrop, moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';
import { Observable, observable, of } from 'rxjs';
import { AngularFirestore, AngularFirestoreCollection, AngularFirestoreDocument } from 'angularfire2/firestore';
import * as firebase from 'firebase';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { EventEmitter } from 'protractor';
import { FormControl } from '@angular/forms';
import { DecimalPipe } from '@angular/common';
import { startWith, map } from 'rxjs/operators';

export interface Chat{
  StartTime: firebase.firestore.Timestamp;
  EndTime: firebase.firestore.Timestamp;
  Flagged: boolean;
  isActive: boolean;
  Rating: number;
  id?: string;
}

export interface Message{
  Flagged: boolean;
  Intent: string;
  MessageText: string;
  Rating: number;
  Response: object;
  Time: firebase.firestore.Timestamp;
  chatID: string;
}

let Chats = [];

function search(text: string, pipe: PipeTransform): Chat[] {
  return Chats.filter(chat => {
    const term = text.toLowerCase();
    return chat.id.toLowerCase().includes(term)
        || pipe.transform(chat.Flagged).includes(term)
        || pipe.transform(chat.Rating).includes(term)
        || pipe.transform(chat.StartTime.toDate()).includes(term);
  });
}

@Component({
  selector: 'app-dragdrop',
  templateUrl: './visitors.component.html',
  styleUrls: ['./visitors.component.css'],
  providers: [DecimalPipe]
})
export class DragdropComponent {
  chatCollectionRef: AngularFirestoreCollection<Chat>;
  chat$: Observable<Chat[]>;

  messageCollectionRef: AngularFirestoreCollection<Message>;
  message$: Observable<Message[]>;

  selectedChat: Observable<Chat>;

  closeResult: string;

  filter = new FormControl('');

  private chatArray=[];

  page = 1;
  pageSize = 10;
  collectionSize = this.chatArray.length;

  p: number = 1;
  searchText;

  // todo = [
  //   'Get to work',
  //   'Pick up groceries',
  //   'Go home',
  //   'Fall asleep'
  // ];

  // done = [
  //   'Get up',
  //   'Brush teeth',
  //   'Take a shower',
  //   'Check e-mail',
  //   'Walk dog'
  // ];

  constructor(private db: AngularFirestore, private modalService: NgbModal, pipe:DecimalPipe) { 
    this.chat$ = this.filter.valueChanges.pipe(
      startWith(''),
      map(text => search(text, pipe))
    );
  }

  ngOnInit() {
    this.showPastChats();
  }

  showPastChats() {
    this.chatCollectionRef = this.db.collection<Chat>('chat', ref => ref.where('isActive', '==', true));
    this.chat$ = this.chatCollectionRef.valueChanges({ idField: 'id'});
    this.chat$.subscribe((data)=>{
      Chats.push(data);
    });
  }

  onSelect(chat, content) {
    this.selectedChat = chat;

    this.messageCollectionRef = this.db.collection<Message>('message', ref => ref.where('chatID', '==', chat.id).orderBy('Time'));
    this.message$ = this.messageCollectionRef.valueChanges();

    this.modalService.open(content, {ariaLabelledBy: 'modal-basic-title'}).result.then((result) => {
      this.closeResult = `Closed with: ${result}`;
    }, (reason) => {
      this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
    });
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return  `with: ${reason}`;
    }
  }
}
