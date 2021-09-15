function forcast(input) {
    let weather = Number(input)

    if (35 < weather) {
        console.log("unknown")
    } else if (26 <= weather) {
        console.log("Hot")
    } else if (20.1 <= weather) {
        console.log("Warm")
    } else if (15 <= weather) {
        console.log("Mild")
    } else if (12 <= weather) {
        console.log("Cool")
    } else if (5 <= weather) {
        console.log("Cold")
    } else { console.log("unknown") }
}

forcast(35)