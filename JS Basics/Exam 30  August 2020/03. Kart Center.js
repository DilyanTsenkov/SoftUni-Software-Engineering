function kart(money, laps, card, kartType) {
    money = Number(money);
    let price = 0;
    if (laps == "five") {
        if (kartType == "Child") {
            price = 7;
        }
        else if (kartType == "Junior") {
            price = 9;
        }
        else if (kartType == "Adult") {
            price = 12;
        }
        else {
            price = 18;
        }
    }
    else {
        if (kartType == "Child") {
            price = 11;
        }
        else if (kartType == "Junior") {
            price = 16;
        }
        else if (kartType == "Adult") {
            price = 21;
        }
        else {
            price = 32;
        }
    }
    if (card == "yes") {
        price *= 0.8;
    }
    let difference = Math.abs(money - price);
    if (money < price) {
        console.log(`You don't have enough money! You need ${difference.toFixed(2)}lv more.`);
    }
    else {
        console.log(`You bought ${kartType} ticket for ${laps} laps. Your change is ${difference.toFixed(2)}lv.`);
    }
}
kart("16", "five", "no", "Adult")