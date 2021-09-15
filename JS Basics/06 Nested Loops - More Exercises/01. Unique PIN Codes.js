function pin(input) {
    let firstNumberStop = Number(input[0]);
    let secondNumberStop = Number(input[1]);
    let thirdNumberStop = Number(input[2]);
    for (let firstDigit = 1; firstDigit <= firstNumberStop; firstDigit++) {
        if (firstDigit % 2 == 0) {
            for (let secondDigit = 2; secondDigit <= secondNumberStop; secondDigit++) {
                if (secondDigit == 2 ||secondDigit == 3 || secondDigit == 5 ||secondDigit == 7) {
                    for (let thirdDigit = 1; thirdDigit <= thirdNumberStop; thirdDigit++) {
                        if (thirdDigit % 2 == 0) {
                            console.log(`${firstDigit} ${secondDigit} ${thirdDigit}`);
                        }
                    }
                }
            }
        }
    }
}
pin([8, 2, 8])