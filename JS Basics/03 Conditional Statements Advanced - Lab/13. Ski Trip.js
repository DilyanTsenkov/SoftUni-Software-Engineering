function ski(days, place, rating) {
    days = Number(days) - 1;
    let price = 0;
    if (days < 10) {
        if (place == "room for one person") {
            price = 18 * days;
        }
        else if (place == "apartment") {
            price = 25 * days * 0.7;
        }
        else if (place == "president apartment") {
            price = 35 * days * 0.9;
        }
    }
    else if (10 <= days && days <= 15) {
        if (place == "room for one person") {
            price = 18 * days;
        }
        else if (place == "apartment") {
            price = 25 * days * 0.65;
        }
        else if (place == "president apartment") {
            price = 35 * days * 0.85;
        }
    }
    else if (days > 15) {
        if (place == "room for one person") {
            price = 18 * days;
        }
        else if (place == "apartment") {
            price = 25 * days * 0.5;
        }
        else if (place == "president apartment") {
            price = 35 * days * 0.80;
        }
    }
    if (rating == "positive") {
        price *= 1.25;
    }
    else {
        price *= 0.9;
    }
    console.log(price.toFixed(2))
}
ski("2",
    "apartment",
    "positive")



