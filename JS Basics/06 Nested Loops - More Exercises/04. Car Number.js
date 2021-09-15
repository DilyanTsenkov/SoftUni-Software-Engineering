function carNum(input) {
    let startInterval = Number(input[0]);
    let endInterval = Number(input[1]);
    let print = "";
    for (let firstDigit = startInterval; firstDigit <= endInterval; firstDigit++) {
        for (let secondDigit = startInterval; secondDigit <= endInterval; secondDigit++) {
            for (let thirdtDigit = startInterval; thirdtDigit <= endInterval; thirdtDigit++) {
                for (let fourthDigit = startInterval; fourthDigit <= endInterval; fourthDigit++) {
                    if (((firstDigit % 2 == 0 && fourthDigit % 2 != 0) || (firstDigit % 2 != 0 && fourthDigit % 2 == 0)) && (firstDigit > fourthDigit) && ((secondDigit + thirdtDigit) % 2 == 0)) {
                        print += (`${firstDigit}${secondDigit}${thirdtDigit}${fourthDigit} `);
                    }
                }
            }
        }
    }
    console.log(print);
}
carNum([5, 8])
