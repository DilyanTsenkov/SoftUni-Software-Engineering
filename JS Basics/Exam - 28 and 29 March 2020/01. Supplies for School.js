function supplies(pens, markers, cleaner, discountPercent) {
    pens = Number(pens);
    markers = Number(markers);
    cleaner = Number(cleaner);
    let costs = pens * 5.8 + markers * 7.2 + cleaner * 1.2;
    let discount = costs * discountPercent / 100;
    let result = costs - discount;
    console.log(result.toFixed(3));
}
supplies("4", "2", "5", "13")