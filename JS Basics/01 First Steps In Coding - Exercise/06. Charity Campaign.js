function charity(input1, input2, input3, input4, input5) {
    let days = Number(input1)
    let chefs = Number(input2)
    let cackes = Number(input3)
    let waffles = Number(input4)
    let pancakes = Number(input5)
    let profit = days * chefs * (cackes * 45 + waffles * 5.8 + pancakes * 3.2)
    let costs = profit / 8
    console.log(profit - costs)
}
charity("131", "5", "9", "33", "46")

