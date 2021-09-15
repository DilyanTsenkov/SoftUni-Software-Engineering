function min(numbers) {
    let n = Number(numbers[0]);
    let minNumber = Number.POSITIVE_INFINITY;
    for (let i = 1; i <= n; i++) {
        let num = Number(numbers[i]);
        if (num < minNumber) {
            minNumber = num;
        }
    }
    console.log(minNumber);
}
min(["2",
"-1",
"-2"])




