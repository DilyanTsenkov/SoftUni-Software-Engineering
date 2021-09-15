function shoping(budget, vcs, chips, rams) {
    budget = Number(budget);
    vcs = Number(vcs);
    chips = Number(chips);
    rams = Number(rams);
    let vcsPrice = vcs * 250
    let chipPrice = vcsPrice * 0.35;
    let ramPrice = vcsPrice * 0.1;
    let costs = vcs * 250 + chips * chipPrice + rams * ramPrice;
    if (vcs > chips) {
        costs *= 0.85;
    }
    let diff = Math.abs(budget - costs);
    if (budget >= costs) {
        console.log(`You have ${diff.toFixed(2)} leva left!`);
    }
    else {
        console.log(`Not enough money! You need ${diff.toFixed(2)} leva more!`);
    }
}
shoping(920.45,3,1,1)F