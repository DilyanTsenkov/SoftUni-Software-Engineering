function karting(input) {
    let index = 0;
    let gold = 0;
    let silver = 0;
    let bronze = 0;
    let bestTime = Number.POSITIVE_INFINITY
    let bestPlayer = "";
    while (true) {
        let name = input[index];
        if (name == "Finish") {
            break;
        }
        index++;
        let minutes = Number(input[index]);
        index++;
        let seconds = Number(input[index]);
        index++;
        let timeInSeconds = seconds + minutes * 60;
        if (timeInSeconds < 55) {
            gold++;
        }
        else if (timeInSeconds >= 55 && timeInSeconds <= 85) {
            silver++;
        }
        else if (timeInSeconds > 85 && timeInSeconds <= 120) {
            bronze++;
        }
        if (bestTime > timeInSeconds) {
            bestTime = timeInSeconds
            bestPlayer = name;
        }
    }
    let bestTimeInminutes = Math.floor(bestTime / 60);
    bestTimeInSeconds = bestTime % 60;
    console.log(`With ${bestTimeInminutes} minutes and ${bestTimeInSeconds} seconds ${bestPlayer} is the winner of the day!`);
    console.log(`Today's prizes are ${gold} Gold ${silver} Silver and ${bronze} Bronze cards!`);
}
karting(["Nick",
    "3",
    "20",
    "Jack",
    "2",
    "45",
    "Sofia",
    "4",
    "10",
    "Viktor",
    "2",
    "52",
    "Finish"]
)