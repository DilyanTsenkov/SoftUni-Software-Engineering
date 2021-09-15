function max(input) {
    let maxNumber = Number.NEGATIVE_INFINITY
    let index = 0;
    while (true) {
        let number = input[index];
        index++;
        if (number == "Stop") {
            console.log(maxNumber);
            break;
        }
        number = Number(number);
        if (number > maxNumber) {
            maxNumber = number;
        }
    }
}
max(["-1",
    "-2",
    "Stop"])




