function yard(yard) {
    let area = Number(yard)
    let pricePerMeter = 7.61
    let price = yard * pricePerMeter
    let discount = price * 18 / 100
    let finalPrice = price - discount
    console.log(`The final price is: ${finalPrice} lv.`)
    console.log(`The discount is: ${discount} lv.`)
}
yard("150")