function wage(input) {
    let row = Number(input[0]);
    let position = Number(input[1]);
    let strawberry = 0;
    let blueberries = 0;
    for (let i = 1; i <= row; i++) {
        for (let n = 1; n <= position; n++) {
            if (i % 2 != 0) {
                strawberry++;
            }
            else if (i % 2 == 0 && n % 3 != 0) {
                blueberries++;
            }
        }
    }
    let profit = 0.8 * (strawberry * 3.5 + blueberries * 5);
    console.log(`Total: ${profit.toFixed(2)} lv.`);
}
wage(["2", "8"])