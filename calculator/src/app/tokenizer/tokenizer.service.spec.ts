import { Add_Token, Closing_Token, Div_Token, Exp_Token, Mul_Token, Num_Token, Opening_Token, Sub_Token, tokenize } from "./tokenizer.service"

import { expect, test, describe } from 'vitest';



describe("TokenizerService", () => {
    test("should tokenize 1 + 2", () => {
        expect(tokenize("1+2")).toEqual([new Num_Token(1), new Add_Token, new Num_Token(2)]);
    });
    test("should tokenize 1  +2^(3+(-4)*5/6)", () => {
        expect(tokenize("1  +2^(3+(-4)*5/6)")).toEqual([
            new Num_Token(1),
            new Add_Token(),
            new Num_Token(2),
            new Exp_Token(),
            new Opening_Token(),
            new Num_Token(3),
            new Add_Token(),
            new Opening_Token(),
            new Sub_Token(),
            new Num_Token(4),
            new Closing_Token(),
            new Mul_Token(),
            new Num_Token(5),
            new Div_Token(),
            new Num_Token(6),
            new Closing_Token(),

        ]);
    });
}
)


// describe("TokenizerService", () => {
//     it("should tokenize 1 + 2", () => {
//         expect(tokenize("1+2")).toEqual([new Num_Token(1), new Add_Token, new Num_Token(2)]);
//     });
//     it("should tokenize 1  +2^(3+(-4)*5/6)", () => {
//         expect(tokenize("1  +2^(3+(-4)*5/6)")).toEqual([
//             new Num_Token(1),
//             new Add_Token(),
//             new Num_Token(2),
//             new Exp_Token(),
//             new Opening_Token(),
//             new Num_Token(3),
//             new Add_Token(),
//             new Opening_Token(),
//             new Sub_Token(),
//             new Num_Token(4),
//             new Closing_Token(),
//             new Mul_Token(),
//             new Num_Token(5),
//             new Div_Token(),
//             new Num_Token(6),
//             new Closing_Token(),

//         ]);
//     });
// }
// )