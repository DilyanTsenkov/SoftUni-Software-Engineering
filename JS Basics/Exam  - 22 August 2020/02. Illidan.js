function illidan(players, playerStrength, IllidanBlood) {
    players = Number(players);
    playerStrength = Number(playerStrength);
    IllidanBlood = Number(IllidanBlood);
    let allPlayersStrength = players * playerStrength;
    let difference = Math.abs(allPlayersStrength - IllidanBlood);
    if (allPlayersStrength < IllidanBlood) {
        console.log(`You are not prepared! You need ${difference} more points.`);
    }
    else {
        console.log(`Illidan has been slain! You defeated him with ${difference} points.`);
    }
}
illidan("15","60","1500")