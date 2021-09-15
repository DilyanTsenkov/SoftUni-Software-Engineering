function tom(days) {
    let workDays = 365 - Number(days);
    let playMinutes = workDays * 63 + Number(days) * 127;
    let result = Math.abs(30000 - playMinutes);
    if (30000 > playMinutes) {
        console.log("Tom sleeps well");
        console.log(`${Math.floor(result / 60)} hours and ${result % 60} minutes less for play`);
    }
    else{
        console.log("Tom will run away");
        console.log(`${Math.floor(result / 60)} hours and ${result % 60} minutes more for play`);
    }
}
tom(20)