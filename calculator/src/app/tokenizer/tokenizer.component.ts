import { Component, OnInit } from '@angular/core';
import { tokenize } from './tokenizer.service';

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
    this.value = tokenize(math_expression);
  }

}
