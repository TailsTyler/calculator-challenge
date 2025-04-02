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
    //what erik left. returns [object Object],[object Object],[object Object]
    // this.value = tokenize(math_expression);

    //my attempt
    this.value = (lex0(tokenize(math_expression)) as Num_Node).value;
    console.log(math_expression);
    console.log(tokenize(math_expression));
    console.log(lex0(tokenize(math_expression)) as Num_Node);
    console.log((lex0(tokenize(math_expression)) as Num_Node).value);
    console.log(this.value);
  }

}
