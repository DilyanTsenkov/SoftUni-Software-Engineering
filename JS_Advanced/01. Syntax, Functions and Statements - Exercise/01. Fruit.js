function calculator(fruit, weight, priceKg) {
    let weightKg = (weight / 1000);
    let money = (weightKg * priceKg);
    console.log(`I need $${money.toFixed(2)} to buy ${weightKg.toFixed(2)} kilograms ${fruit}.`);
}

calculator('orange', 2500, 1.80)
calculator('apple', 1563, 2.35)