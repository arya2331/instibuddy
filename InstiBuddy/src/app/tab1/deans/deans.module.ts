import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { DeansPageRoutingModule } from './deans-routing.module';

import { DeansPage } from './deans.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    DeansPageRoutingModule
  ],
  declarations: [DeansPage]
})
export class DeansPageModule {}
