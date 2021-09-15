function tank(fuel, liters, card) {
    liters = Number(liters)
    let price = 0
    if (fuel == "Gasoline") {
        price = 2.22;
        if (card == "Yes") {
            price = 2.22 - 0.18;
        }
    }
    else if (fuel == "Gas") {
        price = 0.93;
        if (card == "Yes") {
            price = 0.93 - 0.08;
        }
    }
    else if (fuel == "Diesel") {
        price = 2.33
        if (card == "Yes") {
            price = 2.33 - 0.12;
        }
    }
    price *= liters;
    if (20 <= liters & liters <= 25) {
        price *= 0.92;
    }
    else if (liters > 25) {
        price *= 0.9
    }
    console.log(`${price.toFixed(2)} lv.`)
}
tank("Diesel", 19, "No")
