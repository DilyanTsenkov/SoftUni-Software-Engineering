function final(input) {
    let k = Number(input[0]);
    let l = Number(input[1]);
    let m = Number(input[2]);
    let n = Number(input[3]);
    let firstNumber = "";
    let secondNumber = "";
    let counter = 0;
    for (let firstDigitfirstNumber = k; firstDigitfirstNumber <= 8; firstDigitfirstNumber++) {
        if (firstDigitfirstNumber % 2 == 0) {
            for (let secondDigitfirstNumber = 9; secondDigitfirstNumber >= l; secondDigitfirstNumber--) {
                if (secondDigitfirstNumber % 2 != 0) {
                    firstNumber = `${firstDigitfirstNumber}${secondDigitfirstNumber}`;
                    for (let firstDigitSecondNumber = m; firstDigitSecondNumber <= 8; firstDigitSecondNumber++) {
                        if (firstDigitSecondNumber % 2 == 0) {
                            for (let secondDigitSecondNumber = 9; secondDigitSecondNumber >= n; secondDigitSecondNumber--) {
                                if (secondDigitSecondNumber % 2 != 0) {
                                    secondNumber = `${firstDigitSecondNumber}${secondDigitSecondNumber}`;
                                    if (firstNumber === secondNumber) {
                                        console.log("Cannot change the same player.");
                                    }
                                    else {
                                        console.log(`${firstNumber} - ${secondNumber}`);
                                        counter++;
                                        if (counter == 6) {
                                            break;
                                        }
                                    }
                                }
                            }
                            if (counter == 6) {
                                break;
                            }
                        }
                    }
                }
                if (counter == 6) {
                    break;
                }
            }
        }
        if (counter == 6) {
            break;
        }
    }
}
final(["7", "6", "8", "5"])