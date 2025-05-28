import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TokenizerComponent } from './tokenizer.component';
import { Add_Token, Num_Token, tokenize } from './tokenizer.service';
// import { TokenizerComponent } from './tokenizer.component';

describe('TokenizerComponent', () => {
  let component: TokenizerComponent;
  let fixture: ComponentFixture<TokenizerComponent>;

  //runs once per functional test
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TokenizerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TokenizerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  //tests whether component was created
  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('adds 1 + 1 to equal 2', () => {
    component.calculate("1+1");
    expect(component.value).toBe(2);
  });


});
