function pets(days, foodKg, dayDogfoodKg, dayCatFoodKg, dayTurtleFoodG) {
    foodKg = Number(foodKg);
    let neededFood = Number(days) * (Number(dayDogfoodKg) + Number(dayCatFoodKg) + (Number(dayTurtleFoodG) / 1000));
    let result = Math.abs(foodKg - neededFood);
    if (foodKg >= neededFood) {
        console.log(`${Math.floor(result)} kilos of food left.`);
    }
    else {
        console.log(`${Math.ceil(result)} more kilos of food are needed.`);
    }
}
pets(5, 10, 2.1, 0.8, 321)