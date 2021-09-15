function machine(drink, shugar, drinkscount) {
    drinkscount = Number(drinkscount);
    let price = 0;
    if (drink == "Espresso") {
        if (shugar == "Without") {
            price = 0.9;
        }
        else if (shugar == "Normal") {
            price = 1;
        }
        else {
            price = 1.2;
        }
    }
    else if (drink == "Cappuccino") {
        if (shugar == "Without") {
            price = 1;
        }
        else if (shugar == "Normal") {
            price = 1.2;
        }
        else {
            price = 1.6;
        }
    }
    else {
        if (shugar == "Without") {
            price = 0.5;
        }
        else if (shugar == "Normal") {
            price = 0.6;
        }
        else {
            price = 0.7;
        }
    }
    if (shugar == "Without") {
        price *= 0.65;
    }
    if (drink == "Espresso" && drinkscount >= 5) {
        price *= 0.75;
    }
    let totalPrice = drinkscount * price;
    if (totalPrice > 15) {
        totalPrice *= 0.8;
    }
    console.log(`You bought ${drinkscount} cups of ${drink} for ${totalPrice.toFixed(2)} lv.`);
}
machine("Tea", "Extra", "3")