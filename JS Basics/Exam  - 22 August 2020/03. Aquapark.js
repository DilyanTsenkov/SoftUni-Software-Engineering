function aquapark(month, hours, people, dayTime) {
    hours = Number(hours);
    people = Number(people);
    let pricePerHour = 0;
    if (month == "march" || month == "april" || month == "may") {
        if (dayTime == "day") {
            pricePerHour = 10.5;
        }
        else {
            pricePerHour = 8.4;
        }
    }
    else {
        if (dayTime == "day") {
            pricePerHour = 12.6;
        }
        else {
            pricePerHour = 10.2;
        }
    }
    if (people >= 4) {
        pricePerHour *= 0.9;
    }
    if (hours >= 5) {
        pricePerHour *= 0.5;
    }
    let costs = pricePerHour * hours * people;
    console.log(`Price per person for one hour: ${pricePerHour.toFixed(2)}`);
    console.log(`Total cost of the visit: ${costs.toFixed(2)}`);
}
aquapark("july","5","5","night")