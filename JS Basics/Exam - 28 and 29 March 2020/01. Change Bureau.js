function change(bitCoin, yuan, commission) {
    bitCoin = Number(bitCoin);
    yuan = Number(yuan);
    commission = Number(commission);
    let bitCoinInLeva = bitCoin * 1168;
    let yuanInUsd = yuan * 0.15;
    let usdInLeva = yuanInUsd * 1.76;
    let leva = bitCoinInLeva + usdInLeva;
    let euro = leva / 1.95;
    let tax = euro * commission / 100;
    let resul = euro - tax;
    console.log(resul.toFixed(2));
}
change("20", "5678", "2.4")