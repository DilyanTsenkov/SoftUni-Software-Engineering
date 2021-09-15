function fitnes(budget, sex, age, sport) {
    budget = Number(budget);
    age = Number(age);
    let price = 0;
    if (sex == "m") {
        if (sport == "Gym") {
            price = 42;
        }
        else if (sport == "Boxing") {
            price = 41;
        }
        else if (sport == "Yoga") {
            price = 45;
        }
        else if (sport == "Zumba") {
            price = 34;
        }
        else if (sport == "Dances") {
            price = 51;
        }
        else if (sport == "Pilates") {
            price = 39;
        }
    }
    else {
        if (sport == "Gym") {
            price = 35;
        }
        else if (sport == "Boxing") {
            price = 37;
        }
        else if (sport == "Yoga") {
            price = 42;
        }
        else if (sport == "Zumba") {
            price = 31;
        }
        else if (sport == "Dances") {
            price = 53;
        }
        else if (sport == "Pilates") {
            price = 37;
        }
    }
    if (age <= 19) {
        price *= 0.8;
    }
    let diff = price - budget;
    if (budget >= price) {
        console.log(`You purchased a 1 month pass for ${sport}.`);
    }
    else {
        console.log(`You don't have enough money! You need $${diff.toFixed(2)} more.`);
    }
}
fitnes("10",
    "m",
    "50",
    "Pilates"
)