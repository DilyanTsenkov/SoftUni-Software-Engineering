function gabi(input) {
    let index = 0;
    let steps = 0
    while (true) {
        let daySteps = input[index];
        index++;
        if (daySteps == "Going home") {
            daySteps = Number(input[index]);
            steps += daySteps;
            if (steps < 10000) {
                console.log(`${10000 - steps} more steps to reach goal.`);
                break;
            }
            else {
                console.log("Goal reached! Good job!");
                console.log(`${steps - 10000} steps over the goal!`);
                break;
            }
        }
        steps += Number(daySteps);
        if (steps >= 10000) {
            console.log("Goal reached! Good job!");
            console.log(`${steps - 10000} steps over the goal!`);
            break;
        }
    }
}
gabi(["125",
    "250",
    "4000",
    "30",
    "2678",
    "4682"])




