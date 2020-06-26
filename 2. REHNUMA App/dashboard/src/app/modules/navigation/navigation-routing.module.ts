import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { NavComponent } from './components/nav/nav.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { TableComponent } from './components/history/history.component';
import { DragdropComponent } from './components/visitors/visitors.component';
import { AddressComponent } from './components/address/address.component';

const routes: Routes = [
  {
    path: '',
    component: NavComponent,
    children: [
      {
        path: 'dashboard',
        component: DashboardComponent
      },
      {
        path: 'history',
        component: TableComponent
      },
      {
        path: 'visitors',
        component: DragdropComponent
      },
      {
        path: 'address',
        component: AddressComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class NavigationRoutingModule { }
