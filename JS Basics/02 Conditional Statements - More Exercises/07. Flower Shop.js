function shop(magnolias, hyacinths, roses, cacti, gift) {
    let sold = Number(magnolias) * 3.25 + Number(hyacinths) * 4 + Number(roses) * 3.5 + Number(cacti) * 8;
    let profit = sold * 0.95;
    let result = Math.abs(gift - profit);
    if (Number(gift) > profit) {
        console.log(`She will have to borrow ${Math.ceil(result)} leva.`);
    }
    else {
        console.log(`She is left with ${Math.floor(result)} leva.`);
    }
}
shop(15, 7, 5, 10, 100)