import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { Hostel2PageRoutingModule } from './hostel2-routing.module';

import { Hostel2Page } from './hostel2.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    Hostel2PageRoutingModule
  ],
  declarations: [Hostel2Page]
})
export class Hostel2PageModule {}
