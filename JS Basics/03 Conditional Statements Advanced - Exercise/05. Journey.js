function holiday(budget, season) {
    budget = Number(budget);
    let destination = "Bulgaria"
    let placeToSleep = "Camp"
    if (budget <= 100) {
        if (season == "summer") {
            budget *= 0.3;
        }
        else {
            budget *= 0.7;
            placeToSleep = "Hotel";
        }
    }
    else if (budget <= 1000) {
        destination = "Balkans";
        if (season == "summer") {
            budget *= 0.4;
        }
        else {
            budget *= 0.8;
            placeToSleep = "Hotel";
        }
    }
    else {
        destination = "Europe";
        budget *= 0.9;
        placeToSleep = "Hotel";
    }
    console.log(`Somewhere in ${destination}`);
    console.log(`${placeToSleep} - ${budget.toFixed(2)}`)
}
holiday("1500", "summer")