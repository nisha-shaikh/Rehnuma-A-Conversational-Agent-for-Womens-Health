import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';


const routes: Routes = [
  {
    path: 'home',
    loadChildren: () => import('src/app/modules/navigation/navigation.module').then(m => m.NavigationModule)
  },
  {
    path: '',
    loadChildren: () => import('src/app/modules/user/user.module').then(m => m.UserModule)
  },
  {
    path: '**',
    component: PageNotFoundComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
