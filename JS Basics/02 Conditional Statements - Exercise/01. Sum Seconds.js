function sport(firstPlayer, secondPlayer, thirdPlayer) {
    let allPlayersTime = Number(firstPlayer) + Number(secondPlayer) + Number(thirdPlayer)
    let allPlayersMin = Math.trunc(Number(allPlayersTime) / 60);
    let allPlayersSec = allPlayersTime % 60;
    if (allPlayersSec < 10) {
        console.log(`${allPlayersMin}:0${allPlayersSec}`);
    }
    else {
        console.log(`${allPlayersMin}:${allPlayersSec}`);
    }
}
sport("22", "7", "34")