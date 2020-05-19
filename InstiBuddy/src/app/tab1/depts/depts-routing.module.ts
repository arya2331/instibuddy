import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DeptsPage } from './depts.page';

const routes: Routes = [
  {
    path: '',
    component: DeptsPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DeptsPageRoutingModule {}
