function division(number1, number2) {
    number1 = Number(number1);
    number2 = Number(number2);
    let sum = 0;
    let store = [];
    for (number1; number1 <= number2; number1++) {
        if (number1 % 9 == 0) {
            sum += number1;
            store.push(number1);
        }
    }
    console.log(`The sum: ${sum}`);
    console.log(store.join('\n'));
}
division("100", "200")