function specialNum(input) {
    let number = Number(input[0]);
    let print = "";
    for (let numberOne = 1; numberOne <= 9; numberOne++) {
        if (number % numberOne == 0) {
            for (let numberTwo = 1; numberTwo <= 9; numberTwo++) {
                if (number % numberTwo == 0) {
                    for (let numberThree = 1; numberThree <= 9; numberThree++) {
                        if (number % numberThree == 0) {
                            for (let numberFour = 1; numberFour <= 9; numberFour++) {
                                if (number % numberFour == 0) {
                                    print += `${numberOne}${numberTwo}${numberThree}${numberFour} `;

                                }
                            }
                        }
                    }
                }
            }
        }
    }
    console.log(print);
}
specialNum(["16"])