var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var sample = "5 / (sine(333) ^ (4 * (3.2 +  16 - 2))";
// tokenize
// abstact syntacx Tree-- composed of nodes
var Token = /** @class */ (function () {
    function Token() {
    }
    return Token;
}());
var Add_Token = /** @class */ (function (_super) {
    __extends(Add_Token, _super);
    function Add_Token() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return Add_Token;
}(Token));
var Sub_Token = /** @class */ (function (_super) {
    __extends(Sub_Token, _super);
    function Sub_Token() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return Sub_Token;
}(Token));
var Mul_Token = /** @class */ (function (_super) {
    __extends(Mul_Token, _super);
    function Mul_Token() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return Mul_Token;
}(Token));
var Div_Token = /** @class */ (function (_super) {
    __extends(Div_Token, _super);
    function Div_Token() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return Div_Token;
}(Token));
var Exp_Token = /** @class */ (function (_super) {
    __extends(Exp_Token, _super);
    function Exp_Token() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return Exp_Token;
}(Token));
var Trig_Token = /** @class */ (function (_super) {
    __extends(Trig_Token, _super);
    function Trig_Token() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return Trig_Token;
}(Token));
var Num_Token = /** @class */ (function (_super) {
    __extends(Num_Token, _super);
    function Num_Token(value) {
        var _this = _super.call(this) || this;
        _this.value = value;
        return _this;
    }
    return Num_Token;
}(Token));
function tokenize(math_expression) {
    var tokens = [];
    var number_expression = new RegExp('^\d+(\.\d+)?');
    math_expression.trim();
    while (math_expression.length > 0) {
        if (number_expression.test(math_expression)) {
            var a = number_expression.exec(math_expression)[0];
            tokens.push(new Num_Token(Number(a)));
        }
        else if (number_expression[0] == "+") {
            tokens.push(new Add_Token);
        }
        else if (number_expression[0] == "-") {
            tokens.push(new Sub_Token);
        }
        else if (number_expression[0] == "*") {
            tokens.push(new Mul_Token);
        }
        else if (number_expression[0] == "/") {
            tokens.push(new Div_Token);
        }
        else if (number_expression[0] == "^") {
            tokens.push(new Exp_Token);
        }
        math_expression.trim();
    }
    return tokens;
}
console.log(tokenize(" "));
