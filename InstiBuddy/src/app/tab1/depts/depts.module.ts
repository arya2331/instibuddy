import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { DeptsPageRoutingModule } from './depts-routing.module';

import { DeptsPage } from './depts.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    DeptsPageRoutingModule
  ],
  declarations: [DeptsPage]
})
export class DeptsPageModule {}
