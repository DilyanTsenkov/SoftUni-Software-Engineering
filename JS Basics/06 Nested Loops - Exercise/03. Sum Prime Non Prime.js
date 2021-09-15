function specialNumbers(input) {
    let primeSum = 0;
    let nonPrimeSum = 0;
    let index = 0;
    let number = input[index];
    while (number != "stop") {
        if (number < 0) {
            console.log("Number is negative.");
        }
        else {
            let counter = 0;
            for (let i = 2; i <= number; i++) {
                if (number % i == 0) {
                    counter++;
                }
            }
            if (counter > 1) {
                nonPrimeSum += Number(number);
            }
            else {
                primeSum += Number(number);
            }
        }
        index++;
        number = input[index];
    }
    console.log(`Sum of all prime numbers is: ${primeSum}`);
    console.log(`Sum of all non prime numbers is: ${nonPrimeSum}`);
}
specialNumbers(["0",
    "-9",
    "0",
    "stop"])


