function equal(input) {
    let n = Number(input[0]);
    let sum = 0;
    let numTwo = 0;
    let previusSum = 0;
    let difference = 0;
    let maxDifference = Number.NEGATIVE_INFINITY
    for (let i = 1; i <= 2 * n; i++) {
        let numOne = Number(input[i]);
        if (i % 2 == 0) {
            sum = numOne + numTwo;
        }
        numTwo = numOne;
        if (i > 3) {
            difference = Math.abs(sum - previusSum);
            if ((difference > maxDifference) && difference != 0) {
                maxDifference = difference;
            }
        }
        previusSum = sum;
    }
    if (maxDifference == Number.NEGATIVE_INFINITY) {
        console.log(`Yes, value=${sum}`);
    }
    else {
        console.log(`No, maxdiff=${maxDifference}`);
    }
}
equal([3, 1, 2, 0, 3, 4, -1])