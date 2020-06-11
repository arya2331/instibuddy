import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { Hostel2Page } from './hostel2.page';

describe('Hostel2Page', () => {
  let component: Hostel2Page;
  let fixture: ComponentFixture<Hostel2Page>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ Hostel2Page ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(Hostel2Page);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
