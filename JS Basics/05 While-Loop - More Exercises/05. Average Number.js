function average(input) {
    let number = Number(input[0]);
    let sum = 0;
    for (let i = 1; i <= number; i++) {
        let newNumber = Number(input[i]);
        sum += newNumber;
    }
    let averageNumber = sum / number;
    console.log(averageNumber.toFixed(2));
}
average(["4", "3", "2", "4", "2"])