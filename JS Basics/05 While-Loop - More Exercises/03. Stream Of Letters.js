function stream(input) {
    let chr = input[0];
    let index = 0;
    let text = "";
    let o = false;
    let c = false;
    let n = false;
    let counterN = 0;
    let counterC = 0;
    let counterO = 0;
    let textStore = [];
    while (chr != "End") {
        let checkChr = Number(chr.charCodeAt(0));
        if ((64 < checkChr && checkChr < 91) || (96 < checkChr && checkChr < 123)) {
            if (chr == "n") {
                if (counterN == 1) {
                    text += chr;
                    counterN = 0;
                }
                counterN++;
                n = true;
            }
            else if (chr == "o") {
                if (counterO == 1) {
                    text += chr;
                    counterO = 0
                }
                counterO++;
                o = true;
            }
            else if (chr == "c") {
                if (counterC == 1) {
                    text += chr;
                    counterC = 0;
                }
                counterC++;
                c = true;
            }
            else {
                text += chr;
            }
            if (o == true && n == true && c == true) {
                textStore.push(text);
                o = false;
                c = false;
                n = false;
                counterN = 0;
                counterC = 0;
                counterO = 0;
                text = " ";
            }
        }
        index++;
        chr = input[index];
    }
    console.log(textStore.join(""));
}
stream(["H", "n", "e", "l", "l", "o", "o", "c", "t", "c", "h", "o", "e", "r", "e", "n", "e", "End"])