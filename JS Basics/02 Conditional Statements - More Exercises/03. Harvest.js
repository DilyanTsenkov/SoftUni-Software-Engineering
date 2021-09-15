function vineyard(area, grapesPerMeter, wineNeeded, workers) {
    let forWine = Number(area) * 0.4;
    let wine = forWine * Number(grapesPerMeter) / 2.5;
    let result = Math.abs(wine - wineNeeded)
    if (wine < Number(wineNeeded)) {
        console.log(`It will be a tough winter! More ${Math.floor(result)} liters wine needed.`);
    }
    else {
        console.log(`Good harvest this year! Total wine: ${Math.floor(wine)} liters.`);
        console.log(`${Math.ceil(result)} liters left -> ${Math.ceil(result / Number(workers))} liters per person.`);
    }

}
vineyard(650, 2, 175, 3)