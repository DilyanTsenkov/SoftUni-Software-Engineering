function bank(deposit, months) {
    deposit = Number(deposit);
    months = Number(months);
    let simpleRate = deposit;
    let complexRate = deposit;
    let lastMontRate = deposit;
    for (let i = 1; i <= months; i++) {
        simpleRate += deposit * 0.03;
        let monthRate = lastMontRate * 0.027;
        complexRate += monthRate;
        lastMontRate = complexRate;
    }
    console.log(`Simple interest rate: ${simpleRate.toFixed(2)} lv.`);
    console.log(`Complex interest rate: ${complexRate.toFixed(2)} lv.`);
    let difference = Math.abs(simpleRate - complexRate);
    if (simpleRate > complexRate) {
        console.log(`Choose a simple interest rate. You will win ${difference.toFixed(2)} lv.`);
    }
    else {
        console.log(`Choose a complex interest rate. You will win ${difference.toFixed(2)} lv.`);
    }
}
bank("500", "6")