import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TabsPage } from './tabs.page';

const routes: Routes = [
  {
    path: 'tabs',
    component: TabsPage,
    children: [
      {
        path: 'tab1',
        loadChildren: () => import('../tab1/tab1.module').then(m => m.Tab1PageModule)
      },
      { path:'tab1/mainpage', loadChildren: () => import('../tab1/mainpage/mainpage.module').then(m => m.MainpagePageModule)},
      { path:'tab1/depts', loadChildren: () => import('../tab1/depts/depts.module').then(m => m.DeptsPageModule)},
      { path:'tab1/individualcontact', loadChildren: () => import('../tab1/individualcontact/individualcontact.module').then(m => m.IndividualcontactPageModule)},
      { path:'tab1/professors', loadChildren: () => import('../tab1/professors/professors.module').then(m => m.ProfessorsPageModule)},
      {
        path: 'tab2',
        loadChildren: () => import('../tab2/tab2.module').then(m => {
          return m.Tab2PageModule;
        })
      },
      {
        path: 'tab3',
        loadChildren: () => import('../tab3/tab3.module').then(m => m.Tab3PageModule)
      },
      {
        path: '',
        redirectTo: '/tabs/tab1',
        pathMatch: 'full'
      }
    ]
  },
  {
    path: '',
    redirectTo: '/tabs/tab1',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TabsPageRoutingModule {}
