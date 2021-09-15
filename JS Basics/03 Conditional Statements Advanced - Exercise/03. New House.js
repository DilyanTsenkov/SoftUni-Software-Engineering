function home(flowerType, flowerCount, budget) {
    flowerCount = Number(flowerCount);
    budget = Number(budget);
    let price = 0
    switch (flowerType) {
        case "Roses":
            price = 5 * flowerCount;
            if (flowerCount > 80) {
                price *= 0.9;
            }
            break;
        case "Dahlias":
            price = 3.8 * flowerCount;
            if (flowerCount > 90) {
                price *= 0.85;
            }
            break;
        case "Tulips":
            price = 2.8 * flowerCount;
            if (flowerCount > 80) {
                price *= 0.85;
            }
            break;
        case "Narcissus":
            price = 3 * flowerCount;
            if (flowerCount < 120) {
                price *= 1.15;
            }
            break;
        case "Gladiolus":
            price = 2.5 * flowerCount;
            if (flowerCount < 80) {
                price *= 1.20;
            }
            break;
    }
    let difference = Math.abs(budget - price);
    if (budget >= price) {
        console.log(`Hey, you have a great garden with ${flowerCount} ${flowerType} and ${difference.toFixed(2)} leva left.`);
    }
    else {
        console.log(`Not enough money, you need ${difference.toFixed(2)} leva more.`);
    }
}
home("Narcissus", 119, 360)


