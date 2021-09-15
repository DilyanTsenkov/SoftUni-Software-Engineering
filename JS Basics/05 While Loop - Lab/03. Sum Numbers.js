function sumNumbers(input) {
    let targetSum = Number(input[0]);
    let index = 1;
    let sum = 0;
    while (true) {
        let number = Number(input[index]);
        index++;
        sum += number;
        if (targetSum <= sum) {
            console.log(sum);
            break;
        }
    }
}
sumNumbers(["20",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6"])

