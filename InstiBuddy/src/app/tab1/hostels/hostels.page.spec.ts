import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { HostelsPage } from './hostels.page';

describe('HostelsPage', () => {
  let component: HostelsPage;
  let fixture: ComponentFixture<HostelsPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HostelsPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(HostelsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
