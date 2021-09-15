function summer(degrees, time) {
    degrees = Number(degrees);
    let outfit = ""
    let shoes = ""
    if (time == "Morning") {
        if (10 <= degrees && degrees <= 18) {
            outfit = "Sweatshirt";
            shoes = "Sneakers";
        }
        else if (18 < degrees && degrees <= 24) {
            outfit = "Shirt";
            shoes = "Moccasins";
        }
        else {
            outfit = "T-Shirt";
            shoes = "Sandals";
        } 
    }
    else if (time == "Afternoon") {
        if (10 <= degrees && degrees <= 18) {
            outfit = "Shirt";
            shoes = "Moccasins";
        }
        else if (18 < degrees && degrees <= 24) {
            outfit = "T-Shirt";
            shoes = "Sandals";
        }
        else {
            outfit = "Swim Suit";
            shoes = "Barefoot";
        }
    }
    else {
        outfit = "Shirt";
        shoes = "Moccasins";
    }
    console.log(`It's ${degrees} degrees, get your ${outfit} and ${shoes}.`)
}
summer("28", "Evening")

