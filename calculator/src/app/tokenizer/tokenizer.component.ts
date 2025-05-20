import { Component, OnInit } from '@angular/core';
import { tokenize } from './tokenizer.service';
import { lex0, Num_Node } from './lexing.service';
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
    let tokens = tokenize(math_expression);
    if (typeof tokens != "string"){
      let lex = lex0(tokens);
      if(typeof lex != "string"){
        this.value = lex.eval().value;
      }
      else{
        this.value = lex;
      }
    }
    else{
      this.value = tokens;
    }
  }

}
