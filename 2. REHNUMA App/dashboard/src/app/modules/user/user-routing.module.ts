import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SplashScreenComponent } from './components/splash-screen/splash-screen.component';
import { MainScreenComponent } from './components/main-screen/main-screen.component';
import { AboutComponent } from './components/about/about.component';
import { ContactComponent } from './components/contact/contact.component';
import { TeamComponent } from './components/team/team.component';
import { ReferencesComponent } from './components/references/references.component';


const routes: Routes = [
  {
    path: '',
    component: SplashScreenComponent
  },
  {
    path: 'main-screen',
    component: MainScreenComponent
  },
  {
    path: 'about',
    component: AboutComponent
  },
  {
    path: 'team',
    component: TeamComponent
  },
  {
    path: 'contact',
    component: ContactComponent

  },
  {
    path: 'references',
    component: ReferencesComponent

  },
  {
    path: 'admin',
    loadChildren: () => import('src/app/modules/auth/auth.module').then(m => m.AuthModule)
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UserRoutingModule { }
