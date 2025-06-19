Practicing ts and tokenization 

there is another, nested readme


display the ast on the site

for testing run npx jest sanity-check from root

npm commands to run
    npm install --save-dev jest ts-jest typescript
    npm i --save-dev @types/jest
    npm install --save-dev jest-environment-jsdom
    npm install --save-dev jest jest-preset-angular @types/jest ts-jest jest-environment-jsdom zone.js

for using vitest which is newer, instead of jest
    npm install -D vitest
    npm run test
    npm install zone.js --save-dev
    npm install --save-dev happy-dom





testing goal:
    "Positive, zero, and negative values fed into every operation. Then compose every operation with every other operation"

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

