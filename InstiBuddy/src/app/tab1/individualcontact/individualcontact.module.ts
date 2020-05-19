import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { IndividualcontactPageRoutingModule } from './individualcontact-routing.module';

import { IndividualcontactPage } from './individualcontact.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    IndividualcontactPageRoutingModule
  ],
  declarations: [IndividualcontactPage]
})
export class IndividualcontactPageModule {}
