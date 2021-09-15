function parking(input) {
    let days = Number(input[0]);
    let hours = Number(input[1]);
    let tax = 0;
    let totalParkin = 0;
    for (let day = 1; day <= days; day++) {
        let dayParking = 0;
        for (let hour = 1; hour <= hours; hour++) {
            if (day % 2 == 0 && hour % 2 != 0) {
                tax = 2.5;
            }
            else if (day % 2 != 0 && hour % 2 == 0) {
                tax = 1.25;
            }
            else {
                tax = 1;
            }
            dayParking += tax;
        }
        totalParkin += dayParking;
        console.log(`Day: ${day} - ${dayParking.toFixed(2)} leva`);
    }
    console.log(`Total: ${totalParkin.toFixed(2)} leva`);
}
parking([5, 2])