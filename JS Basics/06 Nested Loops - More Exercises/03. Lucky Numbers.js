function lucky(input) {
    let luckyNumber = Number(input[0]);
    let print = "";
    for (let firstDigit = 1; firstDigit <= 9; firstDigit++) {
        for (let secondDigit = 1; secondDigit <= 9; secondDigit++) {
            for (let thirdtDigit = 1; thirdtDigit <= 9; thirdtDigit++) {
                for (let fourthDigit = 1; fourthDigit <= 9; fourthDigit++) {
                    if (((firstDigit + secondDigit) == (thirdtDigit + fourthDigit)) && (luckyNumber % (firstDigit + secondDigit) == 0)) {
                        print += (`${firstDigit}${secondDigit}${thirdtDigit}${fourthDigit} `);

                    }
                }
            }
        }
    }
    console.log(print)
}
lucky([7])