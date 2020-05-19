import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { IndividualcontactPage } from './individualcontact.page';

describe('IndividualcontactPage', () => {
  let component: IndividualcontactPage;
  let fixture: ComponentFixture<IndividualcontactPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IndividualcontactPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(IndividualcontactPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
