function graduation(input) {
    let studentName = input[0];
    let index = 1;
    let score = 0;
    let poorcounter = 0;
    let grade = 1;
    let excluded = false;
    while (grade <= 12) {
        let rate = Number(input[index]);
        if (rate < 4) {
            poorcounter++;
            if (poorcounter == 2) {
                console.log(`${studentName} has been excluded at ${grade} grade`);
                excluded = true;
                break;
            }
        }
        index++;
        if (rate >= 4) {
            grade++;
            score += rate;
        }
    }
    let average = (score / 12).toFixed(2);
    if (excluded == false) {
        console.log(`${studentName} graduated. Average grade: ${average}`);
    }
}
graduation(["Mimi",
    "5",
    "6",
    "5",
    "6",
    "5",
    "6",
    "6",
    "2",
    "3"])