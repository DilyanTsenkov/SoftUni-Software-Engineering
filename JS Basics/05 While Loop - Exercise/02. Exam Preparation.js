function exam(input) {
    let poorScore = input[0];
    let poorScoreCounter = 0;
    let index = 1;
    let counter = 0;
    let scoreSum = 0;
    let average = 0;
    let previousTask = "";
    while (true) {
        let task = input[index];
        index++;
        let score = Number(input[index]);
        index++;
        if (task == "Enough") {
            console.log(`Average score: ${average} `);
            console.log(`Number of problems: ${counter}`);
            console.log(`Last problem: ${previousTask}`)
            break;
        }
        if (score <= 4) {
            poorScoreCounter++;
        }
        if (poorScore == poorScoreCounter) {
            console.log(`You need a break, ${poorScore} poor grades.`);
            break;
        }
        scoreSum += score;
        counter++;
        average = (scoreSum / counter).toFixed(2);
        previousTask = task;
    }
}
exam(["2",
    "Income",
    "3",
    "Game Info",
    "6",
    "Best Player",
    "4"])

