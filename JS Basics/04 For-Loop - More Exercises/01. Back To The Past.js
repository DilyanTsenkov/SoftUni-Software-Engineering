function past(input1, input2) {
    let money = Number(input1);
    let yearToLive = Number(input2);
    let age = 18;
    let costs = 0;
    for (let i = 1800; i <= yearToLive; i++) {
        if (i % 2 == 0) {
            costs += 12000;
        }
        else {
            costs += 12000 + 50 * age;
        }
        age += 1;
    }
    let difference = Math.abs(money - costs);
    if (money >= costs) {
        console.log(`Yes! He will live a carefree life and will have ${difference.toFixed(2)} dollars left.`);
    }
    else {
        console.log(`He will need ${difference.toFixed(2)} dollars to survive.`);
    }
}
past("50000", "1802")