function building(input) {
    let floors = input[0];
    let rooms = input[1];
    let officeOrapartment = "";
    let textStore = [];
    let text = "";
    for (let i = floors; i > 0; i--) {
        for (let n = 0; n < rooms; n++) {
            if (floors == 1 || i == floors) {
                text = (`L${i}${n}`);
                textStore.push(text);
            }
            else if (i % 2 == 0) {
                text = (`O${i}${n}`);
                textStore.push(text);
            }
            else {
                text = (`A${i}${n}`);
                textStore.push(text);
            }
        }
        console.log(textStore.join(" "));
        textStore = [];
    }
}
building(["1", "4"])