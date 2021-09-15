function dishwasher(input) {
    let detergentBottles = Number(input[0]);
    let detergent = detergentBottles * 750;
    let index = 1;
    let counter = 0;
    let plates = 0;
    let pots = 0;
    while (true) {
        counter++;
        let washing = input[index];
        index++;
        if (washing == "End" || detergent < 0) {
            break;
        }
        if (counter % 3 == 0) {
            detergent -= Number(washing) * 15;
            pots += Number(washing)
        }
        else {
            detergent -= Number(washing) * 5;
            plates += Number(washing)
        }
    }
    if (detergent >= 0) {
        console.log("Detergent was enough!");
        console.log(`${plates} dishes and ${pots} pots were washed.`);
        console.log(`Leftover detergent ${detergent} ml.`);
    }
    else {
        console.log(`Not enough detergent, ${Math.abs(detergent)} ml. more necessary!`);
    }
}
dishwasher([2, 53, 65, 55, "End"])