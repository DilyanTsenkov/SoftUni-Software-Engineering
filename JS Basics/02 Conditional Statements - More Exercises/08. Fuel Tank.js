function tank(fuel, liters) {
    let result = String(fuel);
    if (fuel == "Diesel" | fuel == "Gasoline" | fuel == "Gas") {
        if (Number(liters) >= 25) {
            console.log(`You have enough ${result.toLowerCase()}.`);
        }
        else {
            console.log(`Fill your tank with ${result.toLowerCase()}!`);
        }
    }
    else {
        console.log("Invalid fuel!");
    }
}
tank("Gasoline", 25)