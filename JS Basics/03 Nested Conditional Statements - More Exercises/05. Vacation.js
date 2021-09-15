function holiday(budget, season) {
    budget = Number(budget);
    let price = 0;
    let location = "";
    let type = "";
    if (1000 >= budget) {
        type = "Camp";
        if (season == "Summer") {
            price = budget * 0.65;
            location = "Alaska";
        }
        else {
            price = budget * 0.45;
            location = "Morocco";
        }
    }
    else if (1000 < budget && budget <= 3000) {
        type = "Hut";
        if (season == "Summer") {
            price = budget * 0.80;
            location = "Alaska";
        }
        else {
            price = budget * 0.60;
            location = "Morocco";
        }
    }
    else {
        type = "Hotel";
        price = budget * 0.90;
        if (season == "Summer") {
            location = "Alaska";
        }
        else {
            location = "Morocco";
        }
    }
    console.log(`${location} - ${type} - ${price.toFixed(2)}`)
}
holiday(5000, "Winter")