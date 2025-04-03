import { Component, OnInit } from '@angular/core';
import { tokenize } from './tokenizer.service';
import { lex, lex0, Num_Node } from './lexing.service';
import { UnaryOperator } from '@angular/compiler';

@Component({
  selector: 'app-tokenizer',
  templateUrl: './tokenizer.component.html',
  styleUrls: ['./tokenizer.component.css']
})
export class TokenizerComponent implements OnInit {

  value:any = "value";

  constructor() { }

  ngOnInit(): void {
  }

  
  calculate(math_expression:string){
    this.value = lex0(tokenize(math_expression)).eval().value;
  }

}
