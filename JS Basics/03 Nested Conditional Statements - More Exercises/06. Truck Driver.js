function driver(season, km) {
    km = Number(km);
    let profit = 1.45 * km
    if (season == "Spring" || season == "Autumn") {
        if (km <= 5000) {
            profit = 0.75 * km;
        }
        else if (5000 < km && km <= 10000) {
            profit = 0.95 * km;
        }
    }
    else if (season == "Summer") {
        if (km <= 5000) {
            profit = 0.9 * km;
        }
        else if (5000 < km && km <= 10000) {
            profit = 1.1 * km;
        }
    }
    else if (season == "Winter") {
        if (km <= 5000) {
            profit = 1.05 * km;
        }
        else if (5000 < km && km <= 10000) {
            profit = 1.25 * km;
        }
    }
    profit *= 0.9 * 4;
    console.log(profit.toFixed(2))
}
driver("Autumn", 8600)