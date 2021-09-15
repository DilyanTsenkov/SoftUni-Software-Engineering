function sumOfTwo(input) {
    let startInterval = Number(input[0]);
    let endInterval = Number(input[1]);
    let magickNumber = Number(input[2]);
    let combination = 0;
    let combinationFlag = false;
    for (let firstNumber = startInterval; firstNumber <= endInterval; firstNumber++) {
        for (let secondNumber = startInterval; secondNumber <= endInterval; secondNumber++) {
            combination++;
            if (firstNumber + secondNumber == magickNumber) {
                combinationFlag = true;
                console.log(`Combination N:${combination} (${firstNumber} + ${secondNumber} = ${magickNumber})`);
                break;
            }
        }
        if (combinationFlag == true) {
            break;
        }
    }
    if (combinationFlag == false) {
        console.log(`${combination} combinations - neither equals ${magickNumber}`);
    }
}
sumOfTwo([88, 888, 2000])