function camp(season, group, students, nights) {
    students = Number(students);
    nights = Number(nights);
    let price = students * nights;
    let sport = "";
    if (season == "Winter") {
        if (group == "boys") {
            price *= 9.60;
            sport = "Judo";
        }
        else if (group == "girls") {
            price *= 9.60;
            sport = "Gymnastics";
        }
        else {
            price *= 10;
            sport = "Ski";
        }
    }
    else if (season == "Summer") {
        if (group == "boys") {
            price *= 15;
            sport = "Football";
        }
        else if (group == "girls") {
            price *= 15;
            sport = "Volleyball";
        }
        else {
            price *= 20;
            sport = "Swimming";
        }
    }
    else {
        if (group == "boys") {
            price *= 7.2;
            sport = "Tennis";
        }
        else if (group == "girls") {
            price *= 7.2;
            sport = "Athletics";
        }
        else {
            price *= 9.5;
            sport = "Cycling";
        }
    }
    if (students >= 50) {
        price *= 0.5;
    }
    else if (students >= 20) {
        price *= 0.85;
    }
    else if (students >= 10) {
        price *= 0.95;
    }
    console.log(`${sport} ${price.toFixed(2)} lv.`);
}
camp("Spring", "mixed", 17, 14)