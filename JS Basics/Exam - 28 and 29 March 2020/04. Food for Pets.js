function pets(input) {
    let days = Number(input[0]);
    let food = Number(input[1]);
    let index = 2;
    let allDogFood = 0;
    let allCatFood = 0;
    let biscuits = 0
    for (let day = 1; day <= days; day++) {
        let dogFood = Number(input[index]);
        index++;
        let catFood = Number(input[index]);
        index++;
        allDogFood += dogFood;
        allCatFood += catFood;
        if (day % 3 == 0) {
            biscuits += (dogFood + catFood) * 0.1;
        }
    }
    let eatenFood = (allDogFood + allCatFood) / food * 100;
    let percentallDogFood = allDogFood / (allDogFood + allCatFood) * 100;
    let percentallCatfood = allCatFood / (allDogFood + allCatFood) * 100;
    console.log(`Total eaten biscuits: ${Math.round(biscuits)}gr.`);
    console.log(`${eatenFood.toFixed(2)}% of the food has been eaten.`);
    console.log(`${percentallDogFood.toFixed(2)}% eaten from the dog.`);
    console.log(`${percentallCatfood.toFixed(2)}% eaten from the cat.`);
}
pets(["3",
    "500",
    "100",
    "30",
    "110",
    "25",
    "120",
    "35",
])