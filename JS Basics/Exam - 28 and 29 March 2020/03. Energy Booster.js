function booster(fruit, size, count) {
    count = Number(count);
    let price = 0;
    if (fruit == "Watermelon") {
        if (size == "small") {
            price = 2 * 56 * count;
        }
        else {
            price = 5 * 28.7 * count;
        }
    }
    else if (fruit == "Mango") {
        if (size == "small") {
            price = 2 * 36.66 * count;
        }
        else {
            price = 5 * 19.60 * count;
        }
    }
    else if (fruit == "Pineapple") {
        if (size == "small") {
            price = 2 * 42.10 * count;
        }
        else {
            price = 5 * 24.80 * count;
        }
    }
    else {
        if (size == "small") {
            price = 2 * 20 * count;
        }
        else {
            price = 5 * 15.20 * count;
        }
    }
    if (price >= 400 && price <= 1000) {
        price *= 0.85;
    }
    if (price > 1000) {
        price *= 0.5;
    }
    console.log(`${price.toFixed(2)} lv.`);
}
booster("Mango",
    "big",
    "8"
)