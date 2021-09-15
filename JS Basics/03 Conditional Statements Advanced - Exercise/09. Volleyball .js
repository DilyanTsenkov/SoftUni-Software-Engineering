function volleyball(year, p, h) {
    p = Number(p);
    h = Number(h);
    let inSofia = 48 - h;
    let playInSofia = inSofia * 3 / 4;
    let playInP = p * 2 / 3
    let play = playInSofia + playInP + h;
    if (year == "leap") {
        play *= 1.15;
    }
    console.log(Math.floor(play))
}
volleyball("normal",
    "6",
    "13")





