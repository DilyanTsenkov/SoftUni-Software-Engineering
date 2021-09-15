function leap(leapYear, year) {
    leapYear = Number(leapYear);
    year = Number(year);
    for (leapYear; leapYear <= year; leapYear += 4) {
        console.log(leapYear);
    }
}
leap("2020",
    "2032")



