function hospital(numbers) {
    let n = Number(numbers[0]);
    let doctors = 7;
    let dayCounter = 0;
    let treated_patients = 0;
    let untreated_patients = 0;
    for (let i = 1; i <= n; i++) {
        let patients = Number(numbers[i]);
        dayCounter += 1;
        if (dayCounter % 3 == 0) {
            dayCounter = 0;
            if (untreated_patients > treated_patients) {
                doctors += 1;
            }
        }
        if (patients > doctors) {
            treated_patients += doctors;
            untreated_patients += patients - doctors;
        }
        else {
            treated_patients += patients;
        }
    }
    console.log(`Treated patients: ${treated_patients}.`)
    console.log(`Untreated patients: ${untreated_patients}.`)
}
hospital([3, 7, 7, 7])