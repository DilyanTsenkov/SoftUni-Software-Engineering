function agency(city, pack, VIP, days) {
    days = Number(days);
    let price = 0;
    if (city == "Bansko" || city == "Borovets") {
        if (pack == "withEquipment") {
            price = 100;
            if (VIP == "yes") {
                price *= 0.9;
            }
        }
        else {
            price = 80;
            if (VIP == "yes") {
                price *= 0.95;
            }
        }
    }
    else if (city == "Varna" || city == "Burgas") {
        if (pack == "withBreakfast") {
            price = 130;
            if (VIP == "yes") {
                price *= 0.88;
            }
        }
        else {
            price = 100;
            if (VIP == "yes") {
                price *= 0.93;
            }
        }
    }

    if (days > 7) {
        days -= 1;
    }
    let allDPrice = price * days;
    if (days < 1) {
        console.log("Days must be positive number!");
    }
    else if (((city == "Bansko" || city == "Borovets") && (pack == "withEquipment" || pack == "noEquipment")) || ((city == "Varna" || city == "Burgas") && (pack == "noBreakfast" || pack == "withBreakfast"))) {
        console.log(`The price is ${allDPrice.toFixed(2)}lv! Have a nice time!`);
    }
    else {
        console.log("Invalid input!");
    }
}
agency("Burgas", "noBreakfast", "no", "4")