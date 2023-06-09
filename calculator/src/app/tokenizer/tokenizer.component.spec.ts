import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TokenizerComponent } from './tokenizer.component';
import { Add_Token, Num_Token, tokenize } from './tokenizer.service';

describe('TokenizerComponent', () => {
  let component: TokenizerComponent;
  let fixture: ComponentFixture<TokenizerComponent>;

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

  it('should create', () => {
    expect(component).toBeTruthy();
  });


});
