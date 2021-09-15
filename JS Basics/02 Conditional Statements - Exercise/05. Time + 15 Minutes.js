function time(hour, minute) {
    hour = Number(hour) * 60;
    minute = Number(minute);
    let minutes = hour + minute + 15;
    hour = Math.floor(minutes / 60);
    minute = minutes % 60;
    if (hour > 23) {
        hour = 0;
    }
    if (minute < 10) {
        console.log(`${hour}:0${minute}`);
    }
    else {
        console.log(`${hour}:${minute}`);
    }
}
time("12", "49")