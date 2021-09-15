function deposit(input1, input2, input3) {
    let depositSum = Number(input1)
    let depositTerm = Number(input2)
    let divident = Number(input3)
    let sum = depositSum + depositTerm * ((depositSum * divident/100) / 12)
    console.log(sum)
}

deposit("2350","6","7")

