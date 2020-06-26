import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import { AngularFirestore, AngularFirestoreCollection, AngularFirestoreDocument } from 'angularfire2/firestore';
import * as firebase from 'firebase';

declare var Plotly: any;

export interface Chat {
  StartTime: firebase.firestore.Timestamp;
  EndTime: firebase.firestore.Timestamp;
  Flagged: boolean;
  IsActive: boolean;
  Rating: number;
}

export interface Message {
  Flagged: boolean;
  Intent: string;
  MessageText: string;
  Rating: number;
  Response: object;
  Time: firebase.firestore.Timestamp;
  chatID: string;
}

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {

  chatCollectionRef: AngularFirestoreCollection<Chat>;
  chat$: Observable<Chat[]>;

  messageCollectionRef: AngularFirestoreCollection<Message>;
  message$: Observable<Message[]>;

  visitor$: any = 0;
  flagRatio$: any = 0;

  @ViewChild('freqChart', { static: true }) freq: ElementRef;
  @ViewChild('intentChart', { static: true }) intent: ElementRef;

  /** Based on the screen size, switch from standard to one column per row */
  cards = this.breakpointObserver.observe(Breakpoints.Handset).pipe(
    map(({ matches }) => {
      if (matches) {
        return [
          { title: 'Card 1', cols: 1, rows: 1 },
          { title: 'Card 2', cols: 1, rows: 1 },
          { title: 'Card 3', cols: 1, rows: 1 },
          { title: 'Card 4', cols: 1, rows: 1 }
        ];
      }

      return [
        { title: 'Card 1', cols: 2, rows: 1 },
        { title: 'Card 2', cols: 1, rows: 1 },
        { title: 'Card 3', cols: 1, rows: 2 },
        { title: 'Card 4', cols: 1, rows: 1 }
      ];
    })
  );

  constructor(private breakpointObserver: BreakpointObserver, private db: AngularFirestore) { }

  ngOnInit() {
    this.analytics()
    this.freqChart()
    this.intentChart()
  }

  analytics() {

    this.db.collection('chat').get().toPromise().then(snap => {
      this.visitor$ += snap.size; // will return the collection size
    });
  }

  freqChart() {
    const element = this.freq.nativeElement

    this.chatCollectionRef = this.db.collection<Chat>('chat', ref => ref.orderBy('StartTime'));
    this.chat$ = this.chatCollectionRef.valueChanges();

    let date = {};

    let x_values = [];
    let y_values = [];

    this.chat$.subscribe(c => {
      for (let i = 0; i < c.length; i++) {
        let time = c[i].StartTime.toDate().toDateString().split(' ').slice(1).join(' ');
        if (date.hasOwnProperty(`${time}`)) {
          date[`${time}`] += 1;
        } else {
          date[`${time}`] = 1;
        }
      }

      x_values = Object.keys(date).map(elem => new Date(elem));
      y_values = Object.values(date);

      var data = [{
        x: x_values,
        y: y_values,
        mode: 'lines',
        name: 'Number of chats per day'
      }]

      var selectorOptions = {
        buttons: [{
          step: 'month',
          stepmode: 'backward',
          count: 1,
          label: '1m'
        }, {
          step: 'month',
          stepmode: 'backward',
          count: 6,
          label: '6m'
        }, {
          step: 'year',
          stepmode: 'todate',
          count: 1,
          label: 'YTD'
        }, {
          step: 'year',
          stepmode: 'backward',
          count: 1,
          label: '1y'
        }, {
          step: 'all',
        }],
      };

      const style = {
        margin: {
          autoexpand: true,
          margin: 0
        },
        // title: {
        //   text: "Number of chats per day"
        // },
        xaxis: {
          title: 'Time',
          rangeselector: selectorOptions,
          rangeslider: {}
        },
        yaxis: {
          title: 'Number of chats',
          fixedrange: true
        }
      }

      Plotly.newPlot(element, data, style, { responsive: true })
    })
  }

  intentChart() {
    const element = this.intent.nativeElement

    this.messageCollectionRef = this.db.collection<Message>('message');
    this.message$ = this.messageCollectionRef.valueChanges();

    let intent = {};
    let flagged = 0;
    let total = 0;

    let x_values = [];
    let y_values = [];

    this.message$.subscribe(m => {
      for (let i = 0; i < m.length; i++) {
        if (intent.hasOwnProperty(`${m[i].Intent}`)) {
          intent[`${m[i].Intent}`] += 1;
        } else {
          intent[`${m[i].Intent}`] = 1;
        }
        if (m[i].Flagged == true) {
          flagged += 1;
        }
        total += 1;
      }

      this.flagRatio$ = flagged / total * 100;

      x_values = Object.keys(intent).map(elem => elem.replace(/_/g, ' '));
      y_values = Object.values(intent);

      var data = [{
        x: x_values,
        y: y_values,
        type: 'bar',
        name: 'Frequency of intents'
      }]

      const style = {
        title: {
          text: "Frequency of intents"
        },
        xaxis: {
          title: 'Intent name',
          automargin: true,
          type: 'category',
          tickangle: -45
        },
        yaxis: {
          title: 'Frequency',
          automargin: true
        },
        autosize: true,
        autoexpand: true,
        margin: {
          autoexpand: true,
          margin: 0,
        },
        // width: 1000
        width: x_values.length*50
      }

      Plotly.newPlot(element, data, style, { responsive: true })
    })
  }

}