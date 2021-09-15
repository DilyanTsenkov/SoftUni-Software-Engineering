function loading(input) {
    let capacity = Number(input[0]);
    let index = 1;
    let counter = 0;
    let counterTwo=0
    while (true) {
        let suitcase = input[index];
        if (suitcase == "End") {
            console.log(`Congratulations! All suitcases are loaded!`);
            break;
        }
        index++;
        if (counterTwo % 2 == 0 && counterTwo!=0) {
            suitcase *= 1.1;
            counterTwo=0
        }
        if (capacity < suitcase) {
            console.log(`No more space!`);
            break;
        }
        capacity -= suitcase;
        counterTwo++;
        counter++;
        
    }
    console.log(`Statistic: ${counter} suitcases loaded.`);
}
loading(["550",
    "100",
    "252",
    "72", "End"

])