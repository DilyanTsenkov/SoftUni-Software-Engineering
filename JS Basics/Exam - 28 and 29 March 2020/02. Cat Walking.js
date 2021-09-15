function walking(minutes, walks, calories) {
    minutes = Number(minutes);
    walks = Number(walks);
    calories = Number(calories);
    let burnedCalories = (minutes * 5) * walks;
    if (burnedCalories >= calories / 2) {
        console.log(`Yes, the walk for your cat is enough. Burned calories per day: ${burnedCalories}.`);
    }
    else {
        console.log(`No, the walk for your cat is not enough. Burned calories per day: ${burnedCalories}.`);
    }
}
walking("15", "2", "500")