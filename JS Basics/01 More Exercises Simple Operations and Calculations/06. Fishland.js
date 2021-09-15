function fishland(input1, input2, input3, input4, input5) {
    let mackerelPrice = Number(input1)
    let spratPrice = Number(input2)
    let bonitoKg = Number(input3)
    let scadKg = Number(input4)
    let musselsKg = Number(input5)
    let bonitoPrice = mackerelPrice * 1.6
    let scadPrice = spratPrice * 1.8
    let moneyNeeded = bonitoKg * bonitoPrice + musselsKg * 7.5 + scadKg * scadPrice
    console.log(moneyNeeded.toFixed(2))
}
fishland(5.55, 3.57, 4.3, 3.6, 7)