function timeToWalk(steps, footprint, speed) {
    let distanceInKm = steps * footprint / 1000;
    let speedInKmPerSecond = speed / 3600;
    let breaks = Math.floor(distanceInKm / 0.5);
    let breaksInSeconds = breaks * 60;

    let time = distanceInKm / (speedInKmPerSecond) + breaksInSeconds;

    let h = Math.floor(time / 3600);
    let m = Math.floor(time % 3600 / 60);
    let s = Math.ceil(time % 3600 % 60);

    if (h < 10) { h = "0" + h; };
    if (m < 10) { m = "0" + m; };
    if (s < 10) { s = "0" + s; };

    console.log(`${h}:${m}:${s}`)
}

timeToWalk(4000, 0.60, 5)
timeToWalk(2564, 0.70, 5.5)
timeToWalk(200000, 0.70, 5.5)