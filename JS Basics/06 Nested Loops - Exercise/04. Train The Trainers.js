function trainTheTrainers(input) {
    let judges = Number(input[0]);
    let index = 1;
    let presentation = input[index];
    let presentationCounter = 0;
    let totalSum = 0;
    while (presentation != "Finish") {
        index++;
        let presentationSum = 0;
        for (let i = 1; i <= judges; i++) {
            let score = Number(input[index]);
            presentationSum += score;
            index++;
        }
        presentationCounter++;
        let averagePresentationSum = presentationSum / judges;
        console.log(`${presentation} - ${averagePresentationSum.toFixed(2)}.`);
        totalSum += averagePresentationSum;
        presentation = input[index];

    }
    let average = totalSum / presentationCounter;
    console.log(`Student's final assessment is ${average.toFixed(2)}.`);
}
trainTheTrainers(["2",
    "Objects and Classes",
    "5.77",
    "4.23",
    "Dictionaries",
    "4.62",
    "5.02",
    "RegEx",
    "2.88",
    "3.42",
    "Finish"])


