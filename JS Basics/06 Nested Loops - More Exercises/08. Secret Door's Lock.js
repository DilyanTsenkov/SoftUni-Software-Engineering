function lock(input) {
    let hundreds = Number(input[0]);
    let tens = Number(input[1]);
    let entity = Number(input[2]);
    for (let up100 = 1; up100 <= hundreds; up100++) {
        for (let up10 = 1; up10 <= tens; up10++) {
            for (let up1 = 1; up1 <= entity; up1++) {
                if ((up1 % 2 == 0 & up100 % 2 == 0) && (((up10 >= 2) && (up10 <= 7)) && (up10 != 4) && (up10 != 6))) {
                    console.log(`${up100} ${up10} ${up1}`);
                }
            }
        }
    }
}
lock([8, 2, 8])
