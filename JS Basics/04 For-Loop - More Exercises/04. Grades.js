function grades(arg) {
    let students = Number(arg[0]);
    let gradePoor = 0;
    let gradeAverage = 0;
    let gradeGood = 0;
    let gradeVeryGood = 0;
    let success = 0
    for (let i = 1; i <= students; i++) {
        let grade = Number(arg[i]);
        if (2 <= grade && grade < 3) {
            gradePoor += 1;
            success += grade;
        }
        else if (3 <= grade && grade < 4) {
            gradeAverage += 1;
            success += grade;
        }
        else if (4 <= grade && grade < 5) {
            gradeGood += 1;
            success += grade;
        }
        else if (5 <= grade) {
            gradeVeryGood += 1;
            success += grade;
        }
    }
    let averageSuccess = success / students;
    let percentGradePoor = gradePoor / students * 100; 5
    let percentGradeAverage = gradeAverage / students * 100;
    let percentGradeGood = gradeGood / students * 100;
    let percentGradeVeryGood = gradeVeryGood / students * 100;
    console.log(`Top students: ${percentGradeVeryGood.toFixed(2)}%`);
    console.log(`Between 4.00 and 4.99: ${percentGradeGood.toFixed(2)}%`);
    console.log(`Between 3.00 and 3.99: ${percentGradeAverage.toFixed(2)}%`);
    console.log(`Fail: ${percentGradePoor.toFixed(2)}%`);
    console.log(`Average: ${averageSuccess.toFixed(2)}`);
}
grades([6, 2, 3, 4, 5, 6, 2.2])