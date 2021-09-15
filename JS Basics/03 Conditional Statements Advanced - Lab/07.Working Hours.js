function working(hour, day) {
    if (10 <= hour && hour <= 18 && day != "Sunday") {
        console.log("open")
    }
    else {
        console.log("closed")
    }
}
working("11",
    "Sunday")


