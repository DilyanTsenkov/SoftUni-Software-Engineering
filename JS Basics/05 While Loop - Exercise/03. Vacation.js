function holiday(input) {
    let excursion = Number(input[0]);
    let moneyInBank = Number(input[1]);
    let index = 2;
    let daySpendCounter = 0
    let dayCounter = 0
    while (moneyInBank < excursion) {
        let action = input[index];
        index++;
        let moneyAction = Number(input[index]);
        index++;
        dayCounter++;
        if (action == "spend") {
            moneyInBank -= moneyAction;
            if (moneyInBank < 0) {
                moneyInBank = 0;
            }
            daySpendCounter++;
            if (daySpendCounter == 5) {
                console.log("You can't save the money.");
                console.log(`${dayCounter}`);
                break;
            }
        }
        else {
            daySpendCounter = 0;
            moneyInBank += moneyAction;
        }
    }
    if (moneyInBank >= excursion) {
        console.log(`You saved the money for ${dayCounter} days.`);
    }
}
holiday(["2000",
    "1000",
    "spend",
    "1200",
    "save",
    "2000"])



