function trekking(input) {
    let groupOfClimbers = Number(input[0]);
    let index = 1;
    let musalaClimbers = 0;
    let montblancClimbers = 0;
    let kilimanjaroClimbers = 0;
    let k2Climbers = 0;
    let everestClimbers = 0;
    let allClimbers = 0;
    for (let i = 1; i <= groupOfClimbers; i++) {
        let climbers = Number(input[index]);
        index++;
        if (climbers <= 5) {
            musalaClimbers += climbers;
        }
        else if (climbers > 5 && climbers <= 12) {
            montblancClimbers += climbers;
        }
        else if (climbers > 12 && climbers <= 25) {
            kilimanjaroClimbers += climbers;
        }
        else if (climbers > 25 && climbers <= 40) {
            k2Climbers += climbers;
        }
        else if (climbers >= 41) {
            everestClimbers += climbers;
        }
        allClimbers += climbers;
    }
    let percentMusalaClimbers = musalaClimbers / allClimbers * 100;
    let percentMontblancClimbers = montblancClimbers / allClimbers * 100;
    let percentKilimanjaroClimbers = kilimanjaroClimbers / allClimbers * 100;
    let percentK2Climbers = k2Climbers / allClimbers * 100;
    let percentEverestClimbers = everestClimbers / allClimbers * 100;
    console.log(`${percentMusalaClimbers.toFixed(2)}%`);
    console.log(`${percentMontblancClimbers.toFixed(2)}%`);
    console.log(`${percentKilimanjaroClimbers.toFixed(2)}%`);
    console.log(`${percentK2Climbers.toFixed(2)}%`);
    console.log(`${percentEverestClimbers.toFixed(2)}%`);
}
trekking(["5",
    "25",
    "41",
    "31",
    "250",
    "6"
])