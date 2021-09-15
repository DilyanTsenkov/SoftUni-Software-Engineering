function song(input) {
    let controlNumber = Number(input[0]);
    let counter = 0;
    let pass = 0;
    let number = "";
    for (let numberOne = 1; numberOne <= 9; numberOne++) {
        for (let numberTwo = 1; numberTwo <= 9; numberTwo++) {
            for (let numberThree = 1; numberThree <= 9; numberThree++) {
                for (let numberFour = 1; numberFour <= 9; numberFour++) {
                    if ((numberOne < numberTwo) && (numberThree > numberFour)) {
                        if (numberOne * numberTwo + numberThree * numberFour == controlNumber) {
                            number += (`${numberOne}${numberTwo}${numberThree}${numberFour} `);
                            counter++;
                            if (counter == 4) {
                                pass = `${numberOne}${numberTwo}${numberThree}${numberFour}`;
                            }
                        }
                    }
                }
            }
        }
    }
    console.log(number);
    if (counter >= 4) {
        console.log(`Password: ${pass}`);
    }
    else {
        console.log("No!");
    }
}
song(["11"])