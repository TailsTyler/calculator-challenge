import { TokenizerComponent } from './../tokenizer.component';

const tokenizer = new TokenizerComponent();

test('adds 1 + 2 to equal 3', () => {
    expect(tokenizer.calculate("1+1")).toBe(2);
});