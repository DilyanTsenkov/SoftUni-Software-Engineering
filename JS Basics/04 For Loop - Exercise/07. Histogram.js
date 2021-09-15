function histogram(number) {
    let n = Number(number[0]);
    let sum1 = 0;
    let sum2 = 0;
    let sum3 = 0;
    let sum4 = 0;
    let sum5 = 0
    for (let i = 1; i <= n; i++) {
        let num = Number(number[i])
        if (num < 200) {
            sum1 += 1;
        }
        else if (200 <= num && num <= 399) {
            sum2 += 1;
        }
        else if (400 <= num && num <= 599) {
            sum3 += 1;
        }
        else if (600 <= num && num <= 799) {
            sum4 += 1;
        }
        else if (800 <= num) {
            sum5 += 1;
        }
    }
    let percentsum1 = sum1 / n * 100;
    let percentsum2 = sum2 / n * 100;
    let percentsum3 = sum3 / n * 100;
    let percentsum4 = sum4 / n * 100;
    let percentsum5 = sum5 / n * 100;
    console.log(`${percentsum1.toFixed(2)}%`);
    console.log(`${percentsum2.toFixed(2)}%`);
    console.log(`${percentsum3.toFixed(2)}%`);
    console.log(`${percentsum4.toFixed(2)}%`);
    console.log(`${percentsum5.toFixed(2)}%`);
}
histogram(["14",
    "53",
    "7",
    "56",
    "180",
    "450",
    "920",
    "12",
    "7",
    "150",
    "250",
    "680",
    "2",
    "600",
    "200"])



