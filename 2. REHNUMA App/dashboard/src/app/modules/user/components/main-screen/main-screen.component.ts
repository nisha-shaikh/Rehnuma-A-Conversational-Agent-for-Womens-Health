import { Component, OnInit} from '@angular/core';
import { Meta } from '@angular/platform-browser';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-main-screen',
  templateUrl: './main-screen.component.html',
  styleUrls: ['./main-screen.component.css']
})
export class MainScreenComponent implements OnInit {
  constructor(private meta: Meta, private titleService: Title) {
    this.meta.addTag({name: 'viewport', content: 'width = device-width'});
  }
  public setTitle( newTitle: string) {
    this.titleService.setTitle( newTitle );
  }

  ngOnInit() {
    this.setTitle("Rehnuma - Home");
  }

}
