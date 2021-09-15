function shop(chrysanthemums, roses, tulips, season, holiday) {
    chrysanthemums = Number(chrysanthemums);
    roses = Number(roses);
    tulips = Number(tulips);
    let priceChrysanthemums = 0;
    let priceRoses = 0;
    let priceTulips = 0;
    if (season == "Spring" || season == "Summer") {
        priceChrysanthemums = 2 * chrysanthemums;
        priceRoses = 4.1 * roses;
        priceTulips = 2.5 * tulips;
    }
    else {
        priceChrysanthemums = 3.75 * chrysanthemums;
        priceRoses = 4.5 * roses;
        priceTulips = 4.15 * tulips;
    }
    if (holiday == "Y") {
        priceChrysanthemums *= 1.15;
        priceRoses *= 1.15;
        priceTulips *= 1.15;
    }
    let bouquet = priceChrysanthemums + priceRoses + priceTulips;
    if (season == "Spring" && tulips > 7) {
        bouquet *= 0.95;
    }
    if (season == "Winter" && roses >= 10) {
        bouquet *= 0.9;
    }
    if ((roses + tulips + chrysanthemums) > 20) {
        bouquet *= 0.8;
    }
    console.log((bouquet + 2).toFixed(2))
}
shop(10, 10, 10, "Autumn", "N")