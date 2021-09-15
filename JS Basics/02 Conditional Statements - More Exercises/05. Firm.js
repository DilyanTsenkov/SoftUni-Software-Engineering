function firm(neededHours, days, overTimeWorkers) {
    neededHours = Number(neededHours)
    let workDays = Number(days) * 0.9;
    let workHours = workDays * 8;
    let workOverTime = (Number(days) * 2 * Number(overTimeWorkers));
    let totalWorkHours = Math.floor(workHours + workOverTime);
    let result = Math.abs(totalWorkHours - neededHours);
    if (neededHours <= totalWorkHours) {
        console.log(`Yes!${Math.floor(result)} hours left.`);
    }
    else {
        console.log(`Not enough time!${Math.floor(result)} hours needed.`);
    }
}
firm(50, 5, 2)