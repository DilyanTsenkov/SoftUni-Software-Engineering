function holiday(budget, nights, pricePerNight, addcosts) {
    if (Number(nights) > 7) {
        pricePerNight *= 0.95;
    }
    let costs = Number(nights) * Number(pricePerNight) + Number(addcosts) * Number(budget) / 100;
    let difference = Math.abs(Number(budget) - costs);
    if (Number(budget) >= costs) {
        console.log(`Ivanovi will be left with ${difference.toFixed(2)} leva after vacation.`);
    }
    else {
        console.log(`${difference.toFixed(2)} leva needed.`);
    }
}
holiday("500", "7", "66", "15")