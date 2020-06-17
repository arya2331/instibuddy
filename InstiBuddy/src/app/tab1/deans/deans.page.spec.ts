import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { DeansPage } from './deans.page';

describe('DeansPage', () => {
  let component: DeansPage;
  let fixture: ComponentFixture<DeansPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DeansPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(DeansPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
