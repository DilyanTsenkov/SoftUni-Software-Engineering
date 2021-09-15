function game(input) {
    let index = 0;
    let maxPoints = 0;
    let playerMaxPoint = ""
    while (true) {
        let playerName = input[index];
        if (playerName == "Stop") {
            break;
        }
        index++;
        let points = 0;
        for (let i = 0; i < playerName.length; i++) {
            let char = Number(playerName[i].charCodeAt(0));
            let number = input[index];
            if (number == char) {
                points += 10;
            }
            else {
                points += 2;
            }
            index++;
        }
        if (maxPoints <= points) {
            maxPoints = points;
            playerMaxPoint = playerName;
        }
    }
    console.log(`The winner is ${playerMaxPoint} with ${maxPoints} points!`);
}
    game(["Ivan",
        "73",
        "20",
        "98",
        "110",
        "Ivo",
        "80",
        "65",
        "87",
        "Stop"
        ])