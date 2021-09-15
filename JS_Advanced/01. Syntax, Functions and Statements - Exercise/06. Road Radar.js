function radar(speed, area) {
    let speedLimit;
    switch (area) {
        case 'motorway': speedLimit = 130; break;
        case 'interstate': speedLimit = 90; break;
        case 'city': speedLimit = 50; break;
        case 'residential': speedLimit = 20; break;
    }
    if (speed <= speedLimit) {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
    } else {
        let status;
        let difference = Math.abs(speed - speedLimit);
        if (difference <= 20) {
            status = 'speeding';
        }
        else if (20 > difference <= 40) {
            status = 'excessive speeding';
        }
        if (difference > 40) {
            status = 'reckless driving';
        }
        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`);
    }
}

radar(40, 'city')
radar(21, 'residential')
radar(120, 'interstate')
radar(200, 'motorway')