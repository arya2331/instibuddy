import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HostelsPage } from './hostels.page';

const routes: Routes = [
  {
    path: '',
    component: HostelsPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class HostelsPageRoutingModule {}
