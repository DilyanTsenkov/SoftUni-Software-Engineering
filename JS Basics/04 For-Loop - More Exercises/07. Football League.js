function football(input) {
    let StadiumCapacity = Number(input[0]);
    let fans = Number(input[1]);
    let sectorA = 0;
    let sectorB = 0;
    let sectorV = 0;
    let sectorG = 0;
    for (let i = 2; i <= fans + 1; i++) {
        let sector = input[i];
        if (sector == "A") {
            sectorA++;
        }
        else if (sector == "B") {
            sectorB++;
        }
        else if (sector == "G") {
            sectorG++;
        }
        else if (sector == "V") {
            sectorV++;
        }
    }
    let percentSectorA = sectorA / fans * 100;
    let percentSectorB = sectorB / fans * 100;
    let percentSectorV = sectorV / fans * 100;
    let percentSectorG = sectorG / fans * 100;
    let percentfans = fans / StadiumCapacity * 100;
    console.log(`${percentSectorA.toFixed(2)}%`);
    console.log(`${percentSectorB.toFixed(2)}%`);
    console.log(`${percentSectorV.toFixed(2)}%`);
    console.log(`${percentSectorG.toFixed(2)}%`);
    console.log(`${percentfans.toFixed(2)}%`);
}
football([76, 10, "A", "V", "V", "V", "G", "B", "A", "V", "B", "B"])