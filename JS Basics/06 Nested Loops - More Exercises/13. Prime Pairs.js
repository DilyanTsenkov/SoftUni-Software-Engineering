function pairs(input) {
    let startFirstPair = Number(input[0]);
    let startsecondPair = Number(input[1]);
    let diffStartEndFirstPair = Number(input[2]);
    let diffStartEndSecondPair = Number(input[3]);
    let firstPrime = 0;
    let secondPrime = 0;
    let counter = 0;
    for (let firstPair = startFirstPair; firstPair <= (startFirstPair + diffStartEndFirstPair); firstPair++) {
        counter = 0;
        for (let i = 2; i <= firstPair; i++) {
            if (firstPair % i == 0) {
                counter++;
            }
        }
        if (counter == 1) {
            firstPrime = firstPair;
            for (let secondPair = startsecondPair; secondPair <= (startsecondPair + diffStartEndSecondPair); secondPair++) {
                counter = 0;
                for (let i = 2; i <= secondPair; i++) {
                    if (secondPair % i == 0) {
                        counter++;
                    }
                }
                if (counter == 1) {
                    secondPrime = secondPair;
                    console.log(`${firstPrime}${secondPrime}`);
                }
            }
        }
    }
}
pairs([10, 30, 9, 6])