function sequence(input) {
    input = Number(input)
    let digit = 1;
    while (digit <= input) {
        console.log(digit);
        let nextDigit = digit * 2 + 1;
        digit = nextDigit;
    }
}
sequence(["0"])