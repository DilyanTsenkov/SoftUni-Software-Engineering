function game(input) {
    let turns = Number(input[0]);
    let totalPoits = 0;
    let points20 = 0;
    let points30 = 0;
    let points40 = 0;
    let points50 = 0;
    let points100 = 0;
    let pointsinvalid = 0;
    for (let i = 1; i <= turns; i++) {
        let points = Number(input[i]);
        if (0 <= points && points <= 9) {
            totalPoits += points * 0.2;
            points20 += 1;
        }
        else if (10 <= points && points <= 19) {
            totalPoits += points * 0.3;
            points30 += 1;
        }
        else if (20 <= points && points <= 29) {
            totalPoits += points * 0.4;
            points40 += 1;
        }
        else if (30 <= points && points <= 39) {
            totalPoits += 50;
            points50 += 1;
        }
        else if (40 <= points && points <= 50) {
            totalPoits += 100;
            points100 += 1;
        }
        else if (points < 0 || points > 50) {
            pointsinvalid += 1;
            totalPoits /= 2;
        }
    }
    let percentPoints20 = points20 / turns * 100;
    let percentPpoints30 = points30 / turns * 100;
    let percentPpoints40 = points40 / turns * 100;
    let percentPpoints50 = points50 / turns * 100;
    let percentPpoints100 = points100 / turns * 100;
    let percentPpointsinvalid = pointsinvalid / turns * 100;
    console.log(totalPoits.toFixed(2));
    console.log(`From 0 to 9: ${percentPoints20.toFixed(2)}%`);
    console.log(`From 10 to 19: ${percentPpoints30.toFixed(2)}%`);
    console.log(`From 20 to 29: ${percentPpoints40.toFixed(2)}%`);
    console.log(`From 30 to 39: ${percentPpoints50.toFixed(2)}%`);
    console.log(`From 40 to 50: ${percentPpoints100.toFixed(2)}%`);
    console.log(`Invalid numbers: ${percentPpointsinvalid.toFixed(2)}%`);
}
game([10, 43, 57, -12, 23, 12, 0, 50, 40, 30, 20])
