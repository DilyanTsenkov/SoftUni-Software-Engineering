function balance(input) {
    let index = 0;
    let sum = 0;
    while (true) {
        let increase = input[index];
        index++;
        if (increase == "NoMoreMoney") {
            console.log(`Total: ${sum.toFixed(2)}`);
            break;
        }
        if (Number(increase) <= 0) {
            console.log("Invalid operation!")
            console.log(`Total: ${sum.toFixed(2)}`);
            break;
        }
        increase = Number(increase);
        console.log(`Increase: ${increase.toFixed(2)}`)
        sum += increase;
    }
}
balance(["120",
    "45.55",
    "-150"])

