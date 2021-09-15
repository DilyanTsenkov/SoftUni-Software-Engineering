function shoping(pencils, markers, sketchbook, noteBooks) {
    pencils = Number(pencils);
    markers = Number(markers);
    sketchbook = Number(sketchbook);
    noteBooks = Number(noteBooks);
    let costs = pencils * 4.75 + markers * 1.8 + sketchbook * 6.5 + noteBooks * 2.5;
    let discount = costs * 5 / 100;
    let result = costs - discount;
    console.log(`Your total is ${result.toFixed(2)}lv`);
}
shoping("3", "10", "3", "7")