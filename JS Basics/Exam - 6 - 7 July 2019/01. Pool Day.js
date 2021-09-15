function pool(people, tax, sunbedPrice, umbrellaPrice) {
    let entrance = Number(tax) * Number(people);
    let umbrellas = Math.ceil(Number(people) / 2) * umbrellaPrice;
    let sunbed = Math.ceil(Number(people) * 0.75) * Number(sunbedPrice);
    let total = entrance + umbrellas + sunbed;
    console.log(`${total.toFixed(2)} lv.`);
}
pool("50", "6", "8", "4")