function renovation(input) {
    let hight = Number(input[0]);
    let width = Number(input[1]);
    let noPaintingPercent = Number(input[2]);
    let paintingArea = hight * width * 4;
    let noPainting = paintingArea * noPaintingPercent / 100;
    paintingArea = Math.ceil(paintingArea - noPainting);
    let index = 3;
    let paintLiters = input[index];
    while (true) {
        index++;
        if (paintLiters == "Tired!") {
            console.log(`${paintingArea} quadratic m left.`);
            break;
        }
        paintingArea -= Number(paintLiters);
        if (paintingArea < 0) {
            console.log(`All walls are painted and you have ${Math.abs(paintingArea)} l paint left!`);
            break;
        }
        else if (paintingArea == 0) {
            console.log("All walls are painted! Great job, Pesho!");
            break;
        }
        paintLiters = input[index];
    }
}
renovation(["2", "3", "25", "6", "7", "8"])
