function puppy(input) {
    let food = Number(input[0]) * 1000;
    let index = 1;
    while (true) {
        let foodEaten = input[index];
        index++;
        if (foodEaten == "Adopted") {
            break;
        }
        food -= Number(foodEaten);
    }
    if (food >= 0) {
        console.log(`Food is enough! Leftovers: ${food} grams.`);
    }
    else {
        console.log(`Food is not enough. You need ${Math.abs(food)} grams more.`);
    }
}
puppy(["3", "1000", "1000", "1000", "Adopted"])