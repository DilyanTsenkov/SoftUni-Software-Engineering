function cinema(type, rows, columns) {
    rows = Number(rows);
    columns = Number(columns);
    let places = rows * columns;
    let profit = 0
    switch (type) {
        case "Premiere":
            profit = places * 12; break;
        case "Normal":
            profit = places * 7.50; break;
        case "Discount":
            profit = places * 5; break;
    }
    console.log(profit.toFixed(2));
    console.log("leva");
}
cinema("Discount",
    "12",
    "30")


