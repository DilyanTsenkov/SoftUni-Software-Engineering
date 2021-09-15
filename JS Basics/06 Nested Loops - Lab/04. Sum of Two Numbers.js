function twoNumbers(input) {
    let intervalStart = Number(input[0]);
    let intervalEnd = Number(input[1]);
    let magicNumber = Number(input[2]);
    let counter = 0;
    let magicNumberFinder = false;
    for (let i = intervalStart; i <= intervalEnd; i++) {
        for (let n = intervalStart; n <= intervalEnd; n++) {
            let sum = i + n;
            counter++;
            if (sum == magicNumber) {
                console.log(`Combination N:${counter} (${i} + ${n} = ${magicNumber})`);
                magicNumberFinder = true;
                break;
            }
        }
        if (magicNumberFinder == true) {
            break;
        }

    }
    if (magicNumberFinder == false) {
        console.log(`${counter} combinations - neither equals ${magicNumber}`);
    }
}
twoNumbers(["88", "888", "2000"])
