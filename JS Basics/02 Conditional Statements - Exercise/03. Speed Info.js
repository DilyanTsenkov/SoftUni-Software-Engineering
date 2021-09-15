function speedOmeter(speed) {
    speed = Number(speed);
    let result = "";
    if (speed <= 10) {
        result = "slow";
    }
    else if ((10 < speed) & (speed <= 50)) {
        result = "average";
    }
    else if ((50 < speed) & (speed <= 150)) {
        result = "fast";
    }
    else if ((150 < speed) & (speed <= 1000)) {
        result = "ultra fast";
    }
    else if (speed > 1000) {
        result = "extremely fast";
    }
    console.log(result)
}
speedOmeter("8")