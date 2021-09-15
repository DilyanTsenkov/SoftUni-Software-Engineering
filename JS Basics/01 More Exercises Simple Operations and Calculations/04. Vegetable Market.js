function market(input1, input2, input3, input4) {
    let vegetablesPrice = Number(input1)
    let fruitsPrice = Number(input2)
    let vegetablesKg = Number(input3)
    let fruitsKg = Number(input4)
    let profitLv = vegetablesKg * vegetablesPrice + fruitsKg * fruitsPrice
    let profitEu = profitLv / 1.94
    console.log(profitEu.toFixed(2))
}
market(1.5, 2.5, 10, 10)