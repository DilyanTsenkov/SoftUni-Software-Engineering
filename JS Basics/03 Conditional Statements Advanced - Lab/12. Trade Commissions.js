function trade(city, quantity) {
    quantity = Number(quantity);
    let commission = 0
    if (city == "Sofia") {
        if (0 <= quantity && quantity <= 500) {
            commission = quantity * 0.05;
        }
        else if (500 < quantity && quantity <= 1000) {
            commission = quantity * 0.07;
        }
        else if (1000 < quantity && quantity <= 10000) {
            commission = quantity * 0.08;
        }
        else if (quantity > 10000) {
            commission = quantity * 0.12;
        }
    }
    else if (city == "Varna") {
        if (0 <= quantity && quantity <= 500) {
            commission = quantity * 0.045;
        }
        else if (500 < quantity && quantity <= 1000) {
            commission = quantity * 0.075;
        }
        else if (1000 < quantity && quantity <= 10000) {
            commission = quantity * 0.1;
        }
        else if (quantity > 10000) {
            commission = quantity * 0.13;
        }
    }
    else if (city == "Plovdiv") {
        if (0 <= quantity && quantity <= 500) {
            commission = quantity * 0.055;
        }
        else if (500 < quantity && quantity <= 1000) {
            commission = quantity * 0.08;
        }
        else if (1000 <= quantity && quantity <= 10000) {
            commission = quantity * 0.12;
        }
        else if (quantity > 10000) {
            commission = quantity * 0.145;
        }
    }
    if ((city == "Sofia" || city == "Varna" || city == "Plovdiv") && (quantity >= 0)) {
        console.log(commission.toFixed(2));
    }
    else {
        console.log("error");
    }
}
trade("Sofia",
    "501")



