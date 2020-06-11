import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DeansPage } from './deans.page';

const routes: Routes = [
  {
    path: '',
    component: DeansPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DeansPageRoutingModule {}
