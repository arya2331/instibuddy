import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { HostelsPageRoutingModule } from './hostels-routing.module';

import { HostelsPage } from './hostels.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    HostelsPageRoutingModule
  ],
  declarations: [HostelsPage]
})
export class HostelsPageModule {}
