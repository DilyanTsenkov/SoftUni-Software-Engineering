function tournament(input) {
    let days = Number(input[0]);
    let index = 1;
    let money = 0;
    let counter = 0;
    for (let day = 1; day <= days; day++) {
        let dayMoney = 0;
        let dayWin = 0;
        let dayLose = 0;
        while (true) {
            let sport = input[index];
            if (sport == "Finish") {
                break;
            }
            index++;
            let winLose = input[index];
            index++;
            if (winLose == "win") {
                dayWin++;
                dayMoney += 20
            }
            else {
                dayLose++;
            }
        }
        if (dayWin > dayLose) {
            dayMoney *= 1.1;
            counter++;
        }
        money += dayMoney;
        index++;
    }
    if (counter > days / 2) {
        money *= 1.2;
        console.log(`You won the tournament! Total raised money: ${money.toFixed(2)}`);
    }
    else {
        console.log(`You lost the tournament! Total raised money: ${money.toFixed(2)}`);
    }
}
tournament(["3",
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
    "Finish",
])