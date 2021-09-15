function examp(startHour, startMinute, arriveHour, arriveMinute) {
    startHour = Number(startHour);
    startMinute = Number(startMinute);
    arriveHour = Number(arriveHour);
    arriveMinute = Number(arriveMinute);
    let stratInMinutes = startHour * 60 + startMinute;
    let arriveInMinutes = arriveHour * 60 + arriveMinute;
    let differenceInMinutes = Math.abs(stratInMinutes - arriveInMinutes)
    if ((arriveInMinutes + 30) < stratInMinutes) {
        console.log("Early");
        if (differenceInMinutes < 60) {
            console.log(`${differenceInMinutes} minutes before the start`);
        }
        else if (differenceInMinutes % 60 < 10) {
            console.log(`${Math.floor(differenceInMinutes / 60)}:0${differenceInMinutes % 60} hours before the start`);
        }
        else {
            console.log(`${Math.floor(differenceInMinutes / 60)}:${differenceInMinutes % 60} hours before the start`);
        }
    }
    else if (arriveInMinutes > stratInMinutes) {
        console.log("Late");
        if (differenceInMinutes < 60) {
            console.log(`${differenceInMinutes} minutes after the start`);
        }
        else if (differenceInMinutes % 60 < 10) {
            console.log(`${Math.floor(differenceInMinutes / 60)}:0${differenceInMinutes % 60} hours after the start`);
        }
        else {
            console.log(`${Math.floor(differenceInMinutes / 60)}:${differenceInMinutes % 60} hours after the start`);
        }
    }
    else {
        console.log("On time");
        if (arriveInMinutes != stratInMinutes) {
            console.log(`${differenceInMinutes} minutes before the start`)
        }
    }
}
examp("16",
    "00",
    "17",
    "1")
















