import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UserRoutingModule } from './user-routing.module';
import { AboutComponent } from './components/about/about.component';
import { ContactComponent } from './components/contact/contact.component';
import { MainScreenComponent } from './components/main-screen/main-screen.component';
import { SplashScreenComponent } from './components/splash-screen/splash-screen.component';
import { ChatbotRasaModule } from 'angular-chat-widget-rasa';
import { TeamComponent } from './components/team/team.component';
import { ChatPopupComponent } from './components/chat-popup/chat-popup.component';
import { ReferencesComponent } from './components/references/references.component';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';


@NgModule({
  declarations: [
    AboutComponent,
    ContactComponent,
    MainScreenComponent,
    SplashScreenComponent,
    TeamComponent,
    ChatPopupComponent,
    ReferencesComponent,
    NavBarComponent
  ],
  imports: [
    CommonModule,
    UserRoutingModule,
    ChatbotRasaModule,
  ]
})
export class UserModule { }
