export abstract class Token {}
export class Opening_Token extends Token {}
export class Closing_Token extends Token {}
export class Add_Token extends Token {}
export class Sub_Token extends Token {}
export class Mul_Token extends Token {}
export class Div_Token extends Token {}
export class Exp_Token extends Token {}
export class Trig_Token extends Token {}
export class Num_Token extends Token {
    value:number;
    constructor (value:number) {
        super();
        this.value = value;
    }
}

//identify chars as symbols
export function tokenize (math_expression : string) : Token[] {
    let tokens : Token[] = []
    let number_expression : RegExp = new RegExp('^\\d+(\\.\\d+)?');
    math_expression = math_expression.trim()
    while (math_expression.length > 0) {
        if (number_expression.test(math_expression)){
            let a  = number_expression.exec(math_expression)![0];
            tokens.push(new Num_Token(Number(a)));
            math_expression = math_expression.substring(a.length);
        } else if (math_expression[0] == "("){
            tokens.push(new Opening_Token);
            math_expression = math_expression.substring(1);
        } else if (math_expression[0] == ")"){
            tokens.push(new Closing_Token);
            math_expression = math_expression.substring(1);
        } else if (math_expression[0] == "+"){
            tokens.push(new Add_Token);
            math_expression = math_expression.substring(1);
        } else if (math_expression[0] == "-"){
            //ig there should be no Neg_token bc ig only the lexer knows whether something to the left of a '-' is a complete expression    
            tokens.push(new Sub_Token);
            math_expression = math_expression.substring(1);
        } else if (math_expression[0] == "*"){
            tokens.push(new Mul_Token);
            math_expression = math_expression.substring(1);
        } else if (math_expression[0] == "/"){
            tokens.push(new Div_Token);
            math_expression = math_expression.substring(1);
        } else if (math_expression[0] == "^"){
            tokens.push(new Exp_Token);
            math_expression = math_expression.substring(1);
        }
        else {
            console.log(math_expression[0] + " isn't coded for.")
            math_expression = math_expression.substring(1);
        }
        math_expression = math_expression.trim();
    }
    // let l = 0;
    // let r = 0;

    // tokens.forEach(item => {
    // if (item === '(') {
    //     l++;
    // }
    // });
    // tokens.forEach(item => {
    // if (item === ')') {
    //     r++;
    // }
    // });

    // if (tokens) {
    //     this.messageService.add({
    //         key: 'br',
    //         severity: 'info',
    //         detail: 'The Game has not yet begun. Create a Person.',
    //     });
    //     return;
    // }
    return tokens;
}