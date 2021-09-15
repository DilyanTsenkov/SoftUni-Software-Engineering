function cinema(day) {
    let price = 0;
    if (day == "Monday" || day == "Friday" || day == "Tuesday") {
        price = 12;
    }
    else if (day == "Wednesday" || day == "Thursday") {
        price = 14;
    }
    else {
        price = 16;
    }
    console.log(price)
}
cinema("Sunday")