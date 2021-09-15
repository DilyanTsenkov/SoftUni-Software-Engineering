function movie(budget, stat, clothesPrice) {
    budget = Number(budget)
    let decor = 0.1 * budget;
    let clothes = Number(stat) * Number(clothesPrice);
    if (stat > 150) {
        clothes *= 0.9;
    }
    let costs = decor + clothes;
    let difference = Math.abs(budget - costs);
    if (budget >= costs) {
        console.log("Action!");
        console.log(`Wingard starts filming with ${difference.toFixed(2)} leva left.`);
    }
    else {
        console.log("Not enough money!");
        console.log(`Wingard needs ${difference.toFixed(2)} leva more.`);
    }
}
movie("15437.62","186","57.99")



