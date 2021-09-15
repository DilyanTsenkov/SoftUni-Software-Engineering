function wedding(input) {
    let lastSector = Number(input[0].charCodeAt(0));
    let rowsFirstSector = Number(input[1]);
    let placesOdd = Number(input[2]);
    let print = "";
    let counetr = 0;
    for (let sector = 65; sector <= lastSector; sector++) {
        for (let row = 1; row <= (sector - 65 + rowsFirstSector); row++) {
            if (row % 2 != 0) {
                for (let places = 1; places <= placesOdd; places++) {
                    console.log(`${String.fromCharCode(sector)}${row}${String.fromCharCode(places + 96)} `);
                    counetr++;
                }
            }
            else {
                for (let places = 1; places <= (placesOdd + 2); places++) {
                    console.log(`${String.fromCharCode(sector)}${row}${String.fromCharCode(places + 96)} `);
                    counetr++;
                }
            }
        }
    }
    console.log(counetr);
}
wedding(["C", 4, 2])


