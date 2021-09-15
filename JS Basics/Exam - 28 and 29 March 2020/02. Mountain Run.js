function climbing(recordInSec, distanceInMeters, timeInSecForOneMeter) {
    recordInSec = Number(recordInSec);
    distanceInMeters = Number(distanceInMeters);
    timeInSecForOneMeter = Number(timeInSecForOneMeter);
    let slowdown = Math.floor(distanceInMeters / 50) * 30;
    let georgiTimeInSec = distanceInMeters * timeInSecForOneMeter + slowdown;
    let diff = georgiTimeInSec - recordInSec;
    if (georgiTimeInSec < recordInSec) {
        console.log(`Yes! The new record is ${georgiTimeInSec.toFixed(2)} seconds.`);
    }
    else {
        console.log(`No! He was ${diff.toFixed(2)} seconds slower.`);
    }
}
climbing("5554.36", "1340", "3.23")