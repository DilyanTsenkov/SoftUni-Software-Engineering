function tournament(input) {
    let days = Number(input[0]);
    let index = 1;
    let allDaysProfit = 0;
    let dayWinCounter = 0;
    for (let i = 1; i <= days; i++) {
        let dayProfit = 0;
        let winCounetr = 0;
        let loseCounter = 0;
        let sport = input[index];
        while (sport != "Finish") {
            index++;
            let result = input[index];
            if (result == "win") {
                dayProfit += 20;
                winCounetr++;
            }
            else {
                loseCounter++;
            }
            index++;
            sport = input[index];
        }
        if (winCounetr > loseCounter) {
            dayProfit *= 1.1;
            dayWinCounter++;
        }
        allDaysProfit += dayProfit;
        index++;
    }
    if (dayWinCounter > days / 2) {
        allDaysProfit *= 1.2;
        console.log(`You won the tournament! Total raised money: ${allDaysProfit.toFixed(2)}`);
    }
    else {
        console.log(`You lost the tournament! Total raised money: ${allDaysProfit.toFixed(2)}`);
    }
}
tournament
    (["3",
        "darts",
        "lose",
        "handball",
        "lose",
        "judo",
        "win",
        "Finish",
        "snooker",
        "lose",
        "swimming",
        "lose",
        "squash",
        "lose",
        "table tennis",
        "win",
        "Finish",
        "volleyball",
        "win",
        "basketball",
        "win",
        "Finish"
        ])
