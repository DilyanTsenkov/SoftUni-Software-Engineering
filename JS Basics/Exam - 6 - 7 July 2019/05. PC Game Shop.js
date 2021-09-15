function shop(input) {
    let n = Number(input[0]);
    let hearthstoneCounter = 0;
    let forniteCounter = 0;
    let overwatchCounter = 0;
    let otherCounter = 0;
    for (let i = 1; i <= n; i++) {
        let gameName = input[i];
        if (gameName == "Hearthstone") {
            hearthstoneCounter++;
        }
        else if (gameName == "Fornite") {
            forniteCounter++;
        }
        else if (gameName == "Overwatch") {
            overwatchCounter++;
        }
        else {
            otherCounter++;
        }
    }
    let percentHearthstoneCounter = hearthstoneCounter / n * 100;
    let percenforniteCounter = forniteCounter / n * 100;
    let percentOverwatchCounter = overwatchCounter / n * 100;
    let percentotherCounter = otherCounter / n * 100;
    console.log(`Hearthstone - ${percentHearthstoneCounter.toFixed(2)}%`);
    console.log(`Fornite - ${percenforniteCounter.toFixed(2)}%`);
    console.log(`Overwatch - ${percentOverwatchCounter.toFixed(2)}%`);
    console.log(`Others - ${percentotherCounter.toFixed(2)}%`);
}
shop(["3", "Hearthstone", "Diablo 2", "Star Craft 2"])