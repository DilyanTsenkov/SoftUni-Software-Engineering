function circleArea(radius) {
    typeOfRadius = typeof (radius)
    if (typeOfRadius == 'number') {
        let area = radius ** 2 * Math.PI;
        console.log(area.toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${typeOfRadius}.`);
    }
}

circleArea(5)
circleArea('name')