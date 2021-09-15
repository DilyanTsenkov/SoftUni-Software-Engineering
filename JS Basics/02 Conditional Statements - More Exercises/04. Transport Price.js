function student(km, dayNight) {
    let price = 0
    km = Number(km)

    if (km >= 100) {
        price = 0.06 * km;
    }
    else if (km >= 20) {
        price = 0.09 * km;
    }
    else {
        price = 0.7 + 0.9 * km;
        if (dayNight == "day") {
            price = 0.7 + 0.79 * km;
        }
    }
    console.log(price.toFixed(2))
}
student(180, "night")