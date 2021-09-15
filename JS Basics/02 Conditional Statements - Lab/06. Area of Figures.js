function areas(figure, input2, input3) {
    let area = 0;
    if (figure === "square") {
        area = Number(input2) * Number(input2);
    }
    else if (figure === "rectangle") {
        area = Number(input2) * Number(input3);
    }
    else if (figure === "circle") {
        area = Math.PI * Number(input2) * Number(input2);
    }
    else if (figure == "triangle") {
        area = Number(input2) * Number(input3) / 2;
    }
    console.log(area.toFixed(3));
}
areas("rectangle", "7", "2.5")