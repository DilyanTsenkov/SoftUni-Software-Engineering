function report(input) {
    let targetSum = Number(input[0]);
    let index = 1;
    let cardPay = 0;
    let cardCounter = 0;
    let cashPay = 0;
    let cashCounter = 0;
    let transactionCounter = 0;
    let moneyCollect = 0;
    while (true) {
        let product = input[index];
        transactionCounter++;
        if (product == "End") {
            console.log("Failed to collect required money for charity.");
            break;
        }
        product = Number(product);
        if (transactionCounter % 2 == 0) {
            if (product >= 10) {
                cardPay += product;
                cardCounter++;
                moneyCollect += product;
                console.log("Product sold!");
            }
            else {
                console.log("Error in transaction!");
            }
        }
        else {
            if (product <= 100) {
                cashPay += product;
                cashCounter++;
                moneyCollect += product;
                console.log("Product sold!");
            }
            else {
                console.log("Error in transaction!");
            }
        }
        index++;
        if (moneyCollect >= targetSum) {
            let averageCS = cashPay / cashCounter;
            let averageCC = cardPay / cardCounter;
            console.log(`Average CS: ${averageCS.toFixed(2)}`);
            console.log(`Average CC: ${averageCC.toFixed(2)}`);
            break;
        }
    }
}
report([500, 120, 8, 63, 256, 78, 317])