function divide(numbers) {
    let n = Number(numbers[0]);
    let p1 = 0;
    let p2 = 0;
    let p3 = 0;
    for (let i = 1; i <= n; i++) {
        let num = Number(numbers[i]);
        if (num % 3 == 0) {
            p2 += 1;
        }
        if (num % 4 == 0) {
            p3 += 1;
        }
        if (num % 2 == 0) {
            p1 += 1;
        }
    }
    let percentP1 = p1 / n * 100;
    let percentP2 = p2 / n * 100;
    let percentP3 = p3 / n * 100;
    console.log(`${percentP1.toFixed(2)}%`);
    console.log(`${percentP2.toFixed(2)}%`);
    console.log(`${percentP3.toFixed(2)}%`);
}
divide(["3",
    "3",
    "6",
    "9"])

