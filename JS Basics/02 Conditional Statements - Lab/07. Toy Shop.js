function toyShop(excursionPrice, puzzels, dolls, bears, minions, trucks) {
    let profit = Number(puzzels) * 2.6 + Number(dolls) * 3 + Number(bears) * 4.1 + Number(minions) * 8.2 + Number(trucks) * 2;
    let count = Number(puzzels) + Number(dolls) + Number(bears) + Number(minions) + Number(trucks);
    if (count >= 50) {
        profit = profit * 0.75;
    }
    let rent = profit * 0.1;
    let money = profit - rent;
    let difference = Math.abs((money - excursionPrice)).toFixed(2);
    if (money >= excursionPrice) {
        console.log(`Yes! ${difference} lv left.`);
    }
    else {
        console.log(`Not enough money! ${difference} lv needed.`);
    }
}
toyShop("320", "8", "2", "5", "5", "1")