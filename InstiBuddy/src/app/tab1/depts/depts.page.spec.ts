import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { DeptsPage } from './depts.page';

describe('DeptsPage', () => {
  let component: DeptsPage;
  let fixture: ComponentFixture<DeptsPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DeptsPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(DeptsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
