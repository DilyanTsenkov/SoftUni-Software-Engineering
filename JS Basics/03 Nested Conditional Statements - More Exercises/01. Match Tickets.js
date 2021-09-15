function match(budget, category, fans) {
    budget = Number(budget);
    fans = Number(fans);
    let transport = 0;
    let tickets = 0;
    if (fans <= 4) {
        transport = budget * 0.75;
    }
    else if (5 <= fans && fans <= 9) {
        transport = budget * 0.6;
    }
    else if (10 <= fans && fans <= 24) {
        transport = budget * 0.5;
    }
    else if (25 <= fans && fans <= 49) {
        transport = budget * 0.4;
    }
    else if (fans >= 50) {
        transport = budget * 0.25;
    }
    if (category == "VIP") {
        tickets = fans * 499.99;
    }
    else {
        tickets = fans * 249.99;
    }
    let costs = tickets + transport;
    let difference = Math.abs(costs - budget);
    if (budget >= costs) {
        console.log(`Yes! You have ${difference.toFixed(2)} leva left.`)
    }
    else {
        console.log(`Not enough money! You need ${difference.toFixed(2)} leva.`)
    }
}
match(30000, "VIP", 49)