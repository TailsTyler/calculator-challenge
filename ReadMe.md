Practicing ts and tokenization 

there is another, nested readme


display the ast on the site

for testing run npx jest sanity-check from root

npm commands to run
    npm install --save-dev jest ts-jest typescript



tests to pass:
    unknown status:
    
    were working:
        (1)+(1)+(1)
        -(1)
        --1
        1--1
        --(1)
        1-(-1)
        1+(1)
        3-2-1
        -1
        --1
        --1--1
        27^(1/3)
        1-1-1
        

todo:
    testing suite!
    merge branch non destructively??
    how can the if statements here be leaned up?:
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
    add trig?

