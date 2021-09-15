function validator(firstX, firstY, secondX, secondY) {
    let x2 = 0;
    let x1 = firstX;
    let y2 = 0;
    let y1 = firstY;
    let length = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
    if (Number.isInteger(length)) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    } else {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
    }

    x2 = 0;
    x1 = secondX;
    y2 = 0;
    y1 = secondY;
    length = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
    if (Number.isInteger(length)) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    } else {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
    }

    x2 = secondX;
    x1 = firstX;
    y2 = secondY;
    y1 = firstY;
    length = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
    if (Number.isInteger(length)) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`);
    } else {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`);
    }
}


validator(3, 0, 0, 4)
validator(2, 1, 1, 1)