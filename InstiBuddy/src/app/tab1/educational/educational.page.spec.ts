import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { EducationalPage } from './educational.page';

describe('EducationalPage', () => {
  let component: EducationalPage;
  let fixture: ComponentFixture<EducationalPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EducationalPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(EducationalPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
