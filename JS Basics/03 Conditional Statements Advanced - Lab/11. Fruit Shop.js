function shop(fruit, day, quantity) {
    quantity = Number(quantity);
    let price = 0;
    let dayValid = day == "Monday" || day == "Tuesday" || day == "Wednesday" || day == "Thursday " || day == "Friday" || day == "Saturday" || day == "Sunday";
    let fruitValid = fruit == "banana" || fruit == "apple" || fruit == "orange" || fruit == "grapefruit" || fruit == "kiwi" || fruit == "pineapple" || fruit == "grapes";
    if (day == "Sunday" || day == "Saturday") {
        if (fruit == "banana") {
            price = 2.7;
        }
        else if (fruit == "apple") {
            price = 1.25;
        }
        else if (fruit == "orange") {
            price = 0.90;
        }
        else if (fruit == "grapefruit") {
            price = 1.60;
        }
        else if (fruit == "kiwi") {
            price = 3.00;
        }
        else if (fruit == "pineapple") {
            price = 5.60;
        }
        else if (fruit == "grapes") {
            price = 4.20;
        }
    }
    else {
        if (fruit == "banana") {
            price = 2.5;
        }
        else if (fruit == "apple") {
            price = 1.20;
        }
        else if (fruit == "orange") {
            price = 0.85;
        }
        else if (fruit == "grapefruit") {
            price = 1.45;
        }
        else if (fruit == "kiwi") {
            price = 2.70;
        }
        else if (fruit == "pineapple") {
            price = 5.50;
        }
        else if (fruit == "grapes") {
            price = 3.85;
        }
    }
    if (!dayValid || !fruitValid) {
        console.log("error");
    }
    else {
        console.log((price * quantity).toFixed(2));
    }
}
shop("orange", "Sunday", "0.5")




