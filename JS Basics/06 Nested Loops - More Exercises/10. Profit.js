function combination(input) {
    let oneLev = Number(input[0]);
    let twoLev = Number(input[1]);
    let fiveLev = Number(input[2]);
    let sumLev = Number(input[3]);
    for (let i1 = 0; i1 <= oneLev; i1++) {
        for (let i2 = 0; i2 <= twoLev; i2++) {
            for (let i5 = 0; i5 <= fiveLev; i5++) {
                if (i1 + i2 * 2 + i5 * 5 == sumLev) {
                    console.log(`${i1} * 1 lv. + ${i2} * 2 lv. + ${i5} * 5 lv. = ${sumLev} lv.`);
                }
            }
        }
    }
}
combination([5, 3, 1, 7])
