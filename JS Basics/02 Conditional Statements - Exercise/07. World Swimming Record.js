function swimRecord(record, meters, secondsPerMeter) {
    let slowingTime = Math.floor(Number(meters) / 15) * 12.5;
    let swimTime = Number(meters) * Number(secondsPerMeter) + slowingTime;
    let difference = Math.abs(record - swimTime);
    if (swimTime < Number(record)) {
        console.log(`Yes, he succeeded! The new world record is ${swimTime.toFixed(2)} seconds.`);
    }
    else {
        console.log(`No, he failed! He was ${difference.toFixed(2)} seconds slower.`)
    }
}
swimRecord("55555.67","3017","5.03")

