class Token {
}
    
class Add_Token extends Token {
}
class Sub_Token extends Token {
}
class Mul_Token extends Token {
}
class Div_Token extends Token {
}
class Exp_Token extends Token {
}
class Trig_Token extends Token {
}
class Num_Token extends Token {
    value:number;
    constructor (value:number) {
        super();
        this.value = value;
    }
}

export function tokenize (math_expression : string) : Token[] {
    let tokens : Token[] = []
    let number_expression : RegExp = new RegExp('^\\d+(\\.\\d+)?');
    math_expression = math_expression.trim()
    while (math_expression.length > 0) {
        if (number_expression.test(math_expression)){
            let a  = number_expression.exec(math_expression)![0];
            tokens.push(new Num_Token(Number(a)));
            math_expression = math_expression.substring(a.length);
        }
        else if (math_expression[0] == "+"){
            tokens.push(new Add_Token);
            math_expression = math_expression.substring(1);
        }
        else if (math_expression[0] == "-"){
            tokens.push(new Sub_Token);
            math_expression = math_expression.substring(1);
        }
        else if (math_expression[0] == "*"){
            tokens.push(new Mul_Token);
            math_expression = math_expression.substring(1);
        }
        else if (math_expression[0] == "/"){
            tokens.push(new Div_Token);
            math_expression = math_expression.substring(1);
        }
        else if (math_expression[0] == "^"){
            tokens.push(new Exp_Token);
            math_expression = math_expression.substring(1);
        }
        math_expression = math_expression.trim();
    }
    return tokens;
}