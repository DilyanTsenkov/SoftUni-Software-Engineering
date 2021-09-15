function store(processorUSD, videoCardUSD, ramUSD, rams, discount) {
    processorUSD = Number(processorUSD);
    videoCardUSD = Number(videoCardUSD);
    ramUSD = Number(ramUSD);
    rams = Number(rams);
    discount = Number(discount);
    let costsUSD = ((processorUSD + videoCardUSD) * (1 - discount)) + (rams * ramUSD);
    let costsLv = costsUSD * 1.57;
    console.log(`Money needed - ${costsLv.toFixed(2)} leva.`);
}
store("200","100","80","1","0.01")