// import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TokenizerComponent } from './tokenizer.component';
// import { Add_Token, Num_Token, tokenize } from './tokenizer.service';
import { expect, test } from 'vitest';

let component = new TokenizerComponent();

//inital test witho old code commented out
test('adds 1 + 2 to equal 3', () => {
  // expect(component.calculate("1+2")).toBe(3);
   component.calculate("1+2");
  expect(component.value).toBe(3);
})

//+ section
test('-1+-1', () => {
   component.calculate("-1+-1");
  expect(component.value).toBe(-2);
})

test('-1+0', () => {
   component.calculate("-1+0");
  expect(component.value).toBe(-1);
})

test('-1+1', () => {
   component.calculate("-1+1");
  expect(component.value).toBe(0);
})

test('0+0', () => {
   component.calculate("0+0");
  expect(component.value).toBe(0);
})

test('0+1', () => {
   component.calculate("0+1");
  expect(component.value).toBe(1);
})

test('1+1', () => {
   component.calculate("1+1");
  expect(component.value).toBe(2);
})

//- section
test('-1--1', () => {
   component.calculate("-1--1");
  expect(component.value).toBe(0);
})

test('-1-0', () => {
   component.calculate("-1-0");
  expect(component.value).toBe(-1);
})

test('-1-1', () => {
   component.calculate("-1-1");
  expect(component.value).toBe(-2);
})

test('0-0', () => {
   component.calculate("0-0");
  expect(component.value).toBe(0);
})

test('0-1', () => {
   component.calculate("0-1");
  expect(component.value).toBe(-1);
})

test('1-1', () => {
   component.calculate("1-1");
  expect(component.value).toBe(0);
})

//* section
test('-1*-1', () => {
   component.calculate("-1*-1");
  expect(component.value).toBe(1);
})

test('-1*0', () => {
   component.calculate("-1*0");
   //this mod checks for equivalence, eg 0 and -0 are the same
  expect(Object.is(component.value, -0)).toBe(true);
})

test('-1*1', () => {
   component.calculate("-1*1");
  expect(component.value).toBe(-1);
})

test('0*0', () => {
   component.calculate("0*0");
  expect(component.value).toBe(0);
})

test('0*1', () => {
   component.calculate("0*1");
  expect(component.value).toBe(0);
})

test('1*1', () => {
   component.calculate("1*1");
  expect(component.value).toBe(1);
})

// '/' section
test('-1/-1', () => {
   component.calculate("-1/-1");
  expect(component.value).toBe(1);
})

test('-1/0', () => {
   component.calculate("-1/0");
  expect(component.value).toBe(-Infinity);
})

test('-1/1', () => {
   component.calculate("-1/1");
  expect(component.value).toBe(-1);
})

test('0/-1', () => {
   component.calculate("0/-1");
  expect(Object.is(component.value, -0)).toBe(true);
})

test('0/0', () => {
   component.calculate("0/0");
  expect(component.value).toBe(NaN);
})

test('0/1', () => {
   component.calculate("0/1");
  expect(component.value).toBe(0);
})

test('1/-1', () => {
   component.calculate("1/-1");
  expect(component.value).toBe(-1);
})

test('1/0', () => {
   component.calculate("1/0");
  expect(component.value).toBe(Infinity);
})

test('1/1', () => {
   component.calculate("1/1");
  expect(component.value).toBe(1);
})


// describe('TokenizerComponent', () => {
//   let component: TokenizerComponent;
//   let fixture: ComponentFixture<TokenizerComponent>;

//   //runs once per functional test
//   beforeEach(async () => {
//     await TestBed.configureTestingModule({
//       declarations: [ TokenizerComponent ]
//     })
//     .compileComponents();
//   });

//   beforeEach(() => {
//     fixture = TestBed.createComponent(TokenizerComponent);
//     component = fixture.componentInstance;
//     fixture.detectChanges();
//   });

//   //tests whether component was created
//   it('should create', () => {
//     expect(component).toBeTruthy();
//   });

//   it('adds 1 + 1 to equal 2', () => {
//     component.calculate("1+1");
//     expect(component.value).toBe(2);
//   });


// });
