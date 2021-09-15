function lettersCombi(input) {
    let startInterval = Number(input[0].charCodeAt(0));
    let endInterval = Number(input[1].charCodeAt(0));
    let skipLetter = Number(input[2].charCodeAt(0));
    let counter = 0;
    let print = "";
    for (let firstLetter = startInterval; firstLetter <= endInterval; firstLetter++) {
        if (firstLetter == skipLetter) {
            continue;
        }
        for (let secondLetter = startInterval; secondLetter <= endInterval; secondLetter++) {
            if (secondLetter == skipLetter) {
                continue;
            }
            for (let thirdLetter = startInterval; thirdLetter <= endInterval; thirdLetter++) {
                if (thirdLetter == skipLetter) {
                    continue;
                }
                counter++;
                print += (String.fromCharCode(firstLetter) + String.fromCharCode(secondLetter) + String.fromCharCode(thirdLetter) + " ");
            }
        }
    }
    print += counter;
    console.log(print);
}
lettersCombi(["a", "c", "z"])F