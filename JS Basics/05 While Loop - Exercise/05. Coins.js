function vending(input) {
    let change = Number(input) * 100;
    let twoleva = 0;
    let oneleva = 0;
    let coins50 = 0;
    let coins20 = 0;
    let coins10 = 0;
    let coins5 = 0;
    let coins2 = 0;
    let coins1 = 0;
    while (Number(change) > 0) {
        change = Number(change);
        if (change / 200 >= 1) {
            twoleva++;
            change -= 200;
        }
        else if (change / 100 >= 1) {
            oneleva++;
            change -= 100;
        }
        else if (change / 50 >= 1) {
            coins50++;
            change -= 50;
        }
        else if (change / 20 >= 1) {
            coins20++;
            change -= 20;
        }
        else if (change / 10 >= 1) {
            coins10++;
            change -= 10;
        }
        else if (change / 5 >= 1) {
            coins5++;
            change -= 5;
        }
        else if (change / 2 >= 1) {
            coins2++;
            change -= 2;
        }
        else if (change / 1 >= 1) {
            coins1++;
            change -= 1;
        }
        change = change.toFixed(0)
    }
    let coins = twoleva + oneleva + coins50 + coins20 + coins10 + coins5 + coins2 + coins1;
    console.log(coins.toFixed(0));
}
vending(["6.50"])