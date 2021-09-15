function min(input) {
    let minNumber = Number.POSITIVE_INFINITY
    let index = 0;
    while (true) {
        let number = input[index];
        index++;
        if (number == "Stop") {
            console.log(minNumber);
            break;
        }
        number = Number(number);
        if (number < minNumber) {
            minNumber = number;
        }
    }
}
min(["-1",
    "-2",
    "Stop"])



