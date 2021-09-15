function lili(age, laundry, toyPrice) {
    age = Number(age);
    laundry = Number(laundry);
    toyPrice = Number(toyPrice);
    let money = 0
    let toys = 0
    for (let i = 1; i <= age; i++) {
        if (i % 2 == 0) {
            money += i / 0.2;
            money -= 1
        }
        else {
            toys += 1;
        }
    }
    money += toys * toyPrice;
    let difference = Math.abs(laundry - money);
    if (money >= laundry) {
        console.log(`Yes! ${difference.toFixed(2)}`)
    }
    else {
        console.log(`No! ${difference.toFixed(2)}`)
    }
}
lili("21", "1570.98", "3")