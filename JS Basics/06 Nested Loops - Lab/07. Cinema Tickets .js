function cinema(input) {
    let index = 0;
    let movie = input[index];
    let studentTickets = 0;
    let standardTickets = 0;
    let kidTickets = 0;
    let soldTickets = 0;
    let allSoldTickets = 0;
    while (movie != "Finish") {
        index++;
        let freePlaces = Number(input[index]);
        while (freePlaces != soldTickets) {
            index++;
            let ticket = input[index];
            if (ticket == "End") {
                console.log(`${movie} - ${(soldTickets / freePlaces * 100).toFixed(2)}% full.`);
                break;
            }
            else if (ticket == "student") {
                studentTickets++;
                soldTickets++;
            }
            else if (ticket == "standard") {
                standardTickets++;
                soldTickets++;
            }
            else {
                kidTickets++;
                soldTickets++;
            }
        }
        if (freePlaces == soldTickets) {
            console.log(`${movie} - ${(soldTickets / freePlaces * 100).toFixed(2)}% full.`);
        }
        allSoldTickets += soldTickets;
        index++;
        movie = input[index];
        soldTickets = 0;
    }
    let percentStudentTickets = studentTickets / allSoldTickets * 100;
    let percentStandardTickets = standardTickets / allSoldTickets * 100;
    let percentKidTickets = 100 - percentStandardTickets - percentStudentTickets;
    console.log(`Total tickets: ${allSoldTickets}`);
    console.log(`${percentStudentTickets.toFixed(2)}% student tickets.`);
    console.log(`${percentStandardTickets.toFixed(2)}% standard tickets.`);
    console.log(`${percentKidTickets.toFixed(2)}% kids tickets.`);
}
cinema(["Taxi",
    "10",
    "standard",
    "kid",
    "student",
    "student",
    "standard",
    "standard",
    "End",
    "Scary Movie",
    "6",
    "student",
    "student",
    "student",
    "student",
    "student",
    "student",
    "Finish"])


