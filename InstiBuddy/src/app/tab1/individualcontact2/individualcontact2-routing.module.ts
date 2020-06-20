import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { Individualcontact2Page } from './individualcontact2.page';

const routes: Routes = [
  {
    path: '',
    component: Individualcontact2Page
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class Individualcontact2PageRoutingModule {}
