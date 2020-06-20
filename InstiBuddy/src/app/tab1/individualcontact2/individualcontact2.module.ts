import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { Individualcontact2PageRoutingModule } from './individualcontact2-routing.module';

import { Individualcontact2Page } from './individualcontact2.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    Individualcontact2PageRoutingModule
  ],
  declarations: [Individualcontact2Page]
})
export class Individualcontact2PageModule {}
