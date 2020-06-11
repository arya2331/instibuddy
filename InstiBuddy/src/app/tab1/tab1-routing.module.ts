import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Tab1Page } from './tab1.page';

const routes: Routes = [
  {
    path: '',
    component: Tab1Page,
  },  {
    path: 'educational',
    loadChildren: () => import('./educational/educational.module').then( m => m.EducationalPageModule)
  },
  {
    path: 'hostels',
    loadChildren: () => import('./hostels/hostels.module').then( m => m.HostelsPageModule)
  },
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.module').then( m => m.AdminPageModule)
  },
  {
    path: 'admin',
    loadChildren: () => import('./admin/admin.module').then( m => m.AdminPageModule)
  },
  {
    path: 'directors',
    loadChildren: () => import('./directors/directors.module').then( m => m.DirectorsPageModule)
  },
  {
    path: 'deans',
    loadChildren: () => import('./deans/deans.module').then( m => m.DeansPageModule)
  },
  {
    path: 'sections',
    loadChildren: () => import('./sections/sections.module').then( m => m.SectionsPageModule)
  },
  {
    path: 'research',
    loadChildren: () => import('./research/research.module').then( m => m.ResearchPageModule)
  },
  {
    path: 'hostel2',
    loadChildren: () => import('./hostel2/hostel2.module').then( m => m.Hostel2PageModule)
  },
  {
    path: 'deans',
    loadChildren: () => import('./deans/deans.module').then( m => m.DeansPageModule)
  },

  
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class Tab1PageRoutingModule {}
