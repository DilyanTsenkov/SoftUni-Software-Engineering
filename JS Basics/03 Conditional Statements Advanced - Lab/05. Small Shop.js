function shop(product, city, count) {
    count = Number(count);
    let price = 0;
    if (city == "Sofia") {
        if (product == "coffee") {
            price = 0.5;
        }
        else if (product == "water") {
            price = 0.8;
        }
        else if (product == "beer") {
            price = 1.20;
        }
        else if (product == "sweets") {
            price = 1.45;
        }
        else if (product == "peanuts") {
            price = 1.60;
        }
    }
    else if (city == "Plovdiv") {
        if (product == "coffee") {
            price = 0.4;
        }
        else if (product == "water") {
            price = 0.7;
        }
        else if (product == "beer") {
            price = 1.15;
        }
        else if (product == "sweets") {
            price = 1.30;
        }
        else if (product == "peanuts") {
            price = 1.50;
        }
    }
    else if (city == "Varna") {
        if (product == "coffee") {
            price = 0.45;
        }
        else if (product == "water") {
            price = 0.7;
        }
        else if (product == "beer") {
            price = 1.10;
        }
        else if (product == "sweets") {
            price = 1.35;
        }
        else if (product == "peanuts") {
            price = 1.55;
        }
    }
    console.log(price * count)
}
shop("sweets","Sofia","2.23")




