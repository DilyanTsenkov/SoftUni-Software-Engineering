function gestapo(numbers) {
    let n = Number(numbers[0]);
    let selary = Number(numbers[1]);
    for (let i = 2; i <= n + 1; i++) {
        let site = numbers[i];
        if (site == "Facebook") {
            selary -= 150;
        }
        else if (site == "Instagram") {
            selary -= 100;
        }
        else if (site == "Reddit") {
            selary -= 50;
        }
        if (selary <= 0) {
            console.log("You have lost your salary.");
            break;
        }
    }
    if (selary > 0) {
        console.log(selary);
    }
}
gestapo(["10",
    "1500",
    "Facebook",
    "Facebook",
    "Facebook",
    "Facebook",
    "Facebook",
    "Facebook",
    "Facebook",
    "Facebook",
    "Facebook",
    "Facebook"])


