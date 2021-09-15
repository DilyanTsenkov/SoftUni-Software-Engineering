function club(input) {
    let profitTarget = Number(input[0]);
    let index = 1;
    let profit = 0;
    let cocktailName = input[index];
    while (true) {
        let difference = profitTarget - profit;
        if (profitTarget <= profit) {
            console.log("Target acquired.");
            break;
        }
        if (cocktailName == "Party!") {
            console.log(`We need ${difference.toFixed(2)} leva more.`)
            break;
        }
        let cocktailPrice = cocktailName.length;
        index++;
        let cocktails = Number(input[index]);
        let cocktailProfit = Number(cocktailPrice) * cocktails;
        if (cocktailProfit % 2 != 0) {
            cocktailProfit *= 0.75;
        }
        profit += cocktailProfit;
        index++;
        cocktailName = input[index];
    }
    console.log(`Club income - ${profit.toFixed(2)} leva.`);
}
club(["100", "Sidecar", "7", "Mojito", "5", "White Russian", "10"])