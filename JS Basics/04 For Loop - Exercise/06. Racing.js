function racing(fuel, outgo, laps) {
    fuel = Number(fuel);
    outgo = Number(outgo);
    laps = Number(laps);
    for (let i = 1; i < laps; i++) {
        fuel -= outgo;
        outgo += 0.1;
        if (fuel < 0) {
            console.log(`You are out of fuel in round ${i}!`);
            break;
        }
    }
    if (fuel >= 0) {
        console.log("Congrats! You won the race!");
    }
}
racing("100", "20", "5")
