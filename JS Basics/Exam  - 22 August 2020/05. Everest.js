function climbing(input) {
    let hight = 5364;
    let everest = 8848;
    let days = 1;
    let index = 0;
    while (hight < everest) {
        let sleep = input[index];
        if (sleep == "END") {
            break;
        }
        if (sleep == "Yes") {
            if (days == 5) {
                break;
            }
            days += 1;
        }
        index++;
        let meters = Number(input[index]);
        hight += meters;
        index++;
        if (days > 5) {
            break;
        }
    }
    if (hight >= everest) {
        console.log(`Goal reached for ${days} days!`);
    }
    else {
        console.log("Failed!");
        console.log(hight);
    }
}
climbing(["Yes","1000","Yes","1000","Yes","1000","Yes","0","No","484"])