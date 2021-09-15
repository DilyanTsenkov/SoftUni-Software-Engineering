function travel(input) {
    let index = 1;
    while (true) {
        let destination = (input.shift());
        if (destination == "End") {
            break;
        }
        let budget = Number(input.shift());
        let savedMoney = 0;
        while (budget > savedMoney) {
            let money = Number(input.shift());
            savedMoney += money;
            if (budget <= savedMoney) {
                console.log(`Going to ${destination}!`);
                break;
            }
        }
    }
}
travel(["France",
    "2000",
    "300",
    "300",
    "200",
    "400",
    "190",
    "258",
    "360",
    "Portugal",
    "1450",
    "400",
    "400",
    "200",
    "300",
    "300",
    "Egypt",
    "1900",
    "1000",
    "280",
    "300",
    "500",
    "End"])

