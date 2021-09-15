function convertor(input) {
    let degC = Number(input)
    let degF = degC * 1.8 + 32
    console.log(degF.toFixed(2))
}
convertor(-5.5)