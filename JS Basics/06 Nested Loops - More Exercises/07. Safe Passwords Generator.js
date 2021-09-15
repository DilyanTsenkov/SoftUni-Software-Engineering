function generator(input) {
    let a = Number(input[0]);
    let b = Number(input[1]);
    let maxPass = Number(input[2]);
    let maxPassFlag = false;
    let print = "";
    let symbolOne = [];
    let symbolTwo = [];
    let counterOne = 0;
    let counterTwo = 0;
    let counterThree = 0;
    let counterFirstSymbol = 21;
    let counterSecondSymbol = 33;
    for (let firstLastSymbol = 35; firstLastSymbol <= 55; firstLastSymbol++) {
        symbolOne.push(String.fromCharCode(firstLastSymbol));
    }
    for (let secondBeforeLastSymbol = 64; secondBeforeLastSymbol <= 96; secondBeforeLastSymbol++) {
        symbolTwo.push(String.fromCharCode(secondBeforeLastSymbol));
    }
    for (let thirdSymbol = 1; thirdSymbol <= a; thirdSymbol++) {
        for (let fourtSymbol = 1; fourtSymbol <= b; fourtSymbol++) {
            print += symbolOne[counterTwo] + symbolTwo[counterThree] + thirdSymbol + fourtSymbol + symbolTwo[counterThree] + symbolOne[counterTwo] + "|";
            counterOne++;
            counterTwo++;
            counterThree++;
            if (counterTwo == counterFirstSymbol) {
                counterTwo = 0;
            }
            if (counterThree == counterSecondSymbol) {
                counterThree = 0;
            }
            if (counterOne == maxPass) {
                maxPassFlag = true;
                break;
            }
        }
        if (maxPassFlag == true) {
            break;
        }
    }
    console.log(print);
}
generator(["20", "50", "35"])