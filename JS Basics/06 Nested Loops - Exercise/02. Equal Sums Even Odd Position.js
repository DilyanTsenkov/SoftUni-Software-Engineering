function equalSum(input) {
    let firstNumber = Number(input[0]);
    let secondNumber = Number(input[1]);
    let print = [];
    for (firstNumber; firstNumber <= secondNumber; firstNumber++) {
        let number = firstNumber.toString();
        let evenSum = 0;
        let oddSum = 0;
        for (let i = 0; i < number.length; i++) {
            if (i % 2 == 0) {
                oddSum += Number(number[i]);
            }
            else {
                evenSum += Number(number[i]);
            }
        }
        if (oddSum == evenSum) {
            print.push(number);
        }
    } console.log(print.join(" "));
}
equalSum(["299900",
    "300000"])
