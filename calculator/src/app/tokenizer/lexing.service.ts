import { Add_Token, Div_Token, Exp_Token, Mul_Token, Num_Token, Opening_Token, Closing_Token, Sub_Token, Token, Trig_Token } from "./tokenizer.service";


export abstract class Node{
    abstract precedence:number;
    complete_expression = false;
    abstract eval():Num_Node; 
    //display():null;
}
export class Num_Node extends Node{
    precedence:number = 0;
    value:number;
    override complete_expression = true;
    constructor (value:number){
        super();
        this.value = value;

    }
    eval():Num_Node{
        return this;
    }
}
export abstract class Unary_Operator_Node extends Node{
    only_child?:Node;
}
export abstract class Binary_Operator_Node extends Node{
    left_child?:Node;
    right_child?:Node;
    //decide who the children are of a bin node
    /*
    1<+>1
    

    */
    apply_precedence():Binary_Operator_Node {
        console.log("\nthis.left_child!: ", this.left_child!);
        if (this.left_child!.precedence > this.precedence){
            let heir = (this.left_child as Binary_Operator_Node)!;
            let future_right_child:Binary_Operator_Node = this!;
            future_right_child.left_child = (heir as Binary_Operator_Node).right_child;
            future_right_child = (future_right_child as Binary_Operator_Node).apply_precedence();
            (heir as Binary_Operator_Node).right_child = future_right_child;
            return heir;
        }
        else {
            return this;
        }
    }
}

export class Paren_Node extends Unary_Operator_Node{ 
    precedence:number = 1;
    eval():Num_Node{
        return this.only_child!.eval();
    }
}
export class Neg_Node extends Unary_Operator_Node{ 
    precedence:number = 2;
    eval():Num_Node{
        let number_to_negate = this.only_child!.eval();
        number_to_negate.value *=-1;
        return number_to_negate;
    }
}
// export class Trig_Node extends Unary_Operator_Node{ 
//     precedence:number = 3;
// }
export class Exp_Node extends Binary_Operator_Node{ 
    precedence:number = 4;
    eval():Num_Node{
        let base = this.left_child!.eval();
        let exp = this.right_child!.eval();
        return new Num_Node(Math.pow(base.value, exp.value));
    }
}
export class Mul_Node extends Binary_Operator_Node{ 
    precedence:number = 5;
    eval():Num_Node{
        let left = this.left_child!.eval();
        let right = this.right_child!.eval();
        return new Num_Node(left.value * right.value);
    }
}
export class Div_Node extends Binary_Operator_Node{ 
    precedence:number = 5;
    eval():Num_Node{
        let left = this.left_child!.eval();
        let right = this.right_child!.eval();
        return new Num_Node(left.value / right.value);
    }
}
export class Add_Node extends Binary_Operator_Node{ 
    precedence:number = 6;
    eval():Num_Node{
        let left = this.left_child!.eval();
        let right = this.right_child!.eval();
        return new Num_Node(left.value + right.value);
    }
}
export class Sub_Node extends Binary_Operator_Node{ 
    precedence:number = 6;
    eval():Num_Node{
        let left = this.left_child!.eval();
        let right = this.right_child!.eval();
        return new Num_Node(left.value - right.value);
    }
}

//tokens to ast
export function lex0 (tokens : Token[]) : Node {
    let tokens_again = tokens;
    let wl:Node[] = [];
    for (let i:number = 0; i < tokens_again.length; i++) {
        if (tokens_again[i] instanceof Num_Token) {
            let i_as_node = new Num_Node((tokens_again[i] as Num_Token).value);
            wl.push(i_as_node);
            if (wl.length == 1){
                continue;
            }
            else {
                let look_for_incomplete_expressions_in_wl = true;
                while(look_for_incomplete_expressions_in_wl){
                    if (wl[wl.length-2] instanceof Binary_Operator_Node){
                        if (wl.length >= 3 && wl[wl.length-3].complete_expression){
                            let to_become_right_child = wl.pop();
                            let x = wl.pop()!;
                            (x as Binary_Operator_Node).right_child = to_become_right_child;
                            (x as Binary_Operator_Node).left_child = wl.pop();
                            x.complete_expression = true;
                            wl.push(x);
                            (x as Binary_Operator_Node).apply_precedence();
                        }
                        else{
                            //erik how do i not reach this for 1+2
                            console.log("\n the i_as_node is a num but the wl.length < 2 or not wl[-2].complete_expression");
                        }
                    } else if (wl[wl.length-2] instanceof Neg_Node && wl[wl.length-1].complete_expression){
                        (wl[wl.length-2] as Unary_Operator_Node).only_child = wl[wl.length-1];
                        wl[wl.length-2].complete_expression = true;
                        wl.pop();
                    }
                    // else if (wl[wl.length-2] instanceof Paren_Node && wl[wl.length-1].complete_expression){
                    //     (wl[wl.length-2] as Unary_Operator_Node).only_child = wl[wl.length-1];
                    //     wl[wl.length-2].complete_expression = true;
                    //     wl.pop();
                    // }
                    else{ //is num... 2 nums adjacent is bad
                        // console.log("\nThese 2 nums are next to each other in the wl! Not good. Here is the wl: ", wl,
                        //     "\n here is the i_as_node: ", i_as_node);
                        look_for_incomplete_expressions_in_wl = false;
                    }
                }
            }
        }
        else if (tokens_again[i] instanceof Closing_Token){
            let should_be_a_complete_expression = wl.pop();
            let should_be_a_opener = wl.pop();
            if (should_be_a_complete_expression?.complete_expression && should_be_a_opener instanceof Paren_Node) {
                let to_push = should_be_a_opener;
                to_push.only_child = should_be_a_complete_expression;
                to_push.complete_expression = true;
                wl.push(to_push);
                //eg 1+(1) is now 1+1 in the wl; must consolidate the +
                if(wl.length > 1){
                    let i = 0;
                    while (wl[i]){
                        if(wl[i] instanceof Binary_Operator_Node && !wl[i].complete_expression){
                            (wl[i] as Binary_Operator_Node).left_child = wl[i-1];
                            (wl[i] as Binary_Operator_Node).right_child = wl[i+1];
                            //remove the left child from wl
                            wl.splice(i - 1, 1);
                            //consider how the indecies change
                            i -= 1;
                            //remove the right child from wl
                            wl.splice(i + 1, 1);
                            wl[i].complete_expression = true;
                        }
                        //this section addresses eg -(1)
                        else if (wl[i] instanceof Neg_Node && !wl[i].complete_expression && wl[i+1] && wl[i+1].complete_expression){
                            (wl[i] as Unary_Operator_Node).only_child = wl[i+1];
                            wl.splice(i + 1, 1);
                            //remove the right child from wl
                            wl.splice(i + 1, 1);
                            wl[i].complete_expression = true;
                        }
                        i+=1;
                    }
                }
            }
        }
        else{
            if (tokens_again[i] instanceof Sub_Token) {
                //the lexer must identify Sub_Tokens as either actual sub nodes, or, instead, as neg nodes
                //if there is a complete expression to the left, it's a sub
                //eg (complex but complete expression)-1
                if(wl[0] && wl[wl.length - 1].complete_expression){
                    wl.push(new Sub_Node()); 
                    continue;
                }
                //if there is not, it's a neg
                //eg 2^-1 = .5, 1--1 = 2, 1+-1 = 0
                //and if there is nothing to the left, it's a neg
                //eg -1+2 = 1
                wl.push(new Neg_Node()); 
            } else if (tokens_again[i] instanceof Add_Token) {
                wl.push(new Add_Node()); 
            } else if (tokens_again[i] instanceof Mul_Token) {
                wl.push(new Mul_Node()); 
            } else if (tokens_again[i] instanceof Div_Token) {
                wl.push(new Div_Node()); 
            } else if (tokens_again[i] instanceof Exp_Token) {
                wl.push(new Exp_Node()); 
            // } else if (tokens_again[i] instanceof Trig_Token) {
            //     wl.push(new Trig_Node()); 
            } else if (tokens_again[i] instanceof Opening_Token) {
                wl.push(new Paren_Node()); 
            }
        }
    }
    if(wl.length != 1){
        console.log("\nNot exactly one tree treturned: maybe baf parentheses")
    }
    return wl[0];
}


