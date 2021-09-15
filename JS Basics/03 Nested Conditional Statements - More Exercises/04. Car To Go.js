function car(budget, season) {
    budget = Number(budget);
    let category = ""
    let type = ""
    let price = 0
    if (budget <= 100) {
        category = "Economy class";
        if (season == "Summer") {
            type = "Cabrio";
            price = budget * 0.35;
        }
        else {
            type = "Jeep";
            price = budget * 0.65;
        }
    }
    else if (100 < budget && budget <= 500) {
        category = "Compact class";
        if (season == "Summer") {
            type = "Cabrio";
            price = budget * 0.45;
        }
        else {
            type = "Jeep";
            price = budget * 0.8;
        }
    }
    else {
        category = "Luxury class";
        type = "Jeep";
        price = budget * 0.9;
    }
    console.log(category);
    console.log(`${type} - ${price.toFixed(2)}`)
}
car(99.99, "Summer")