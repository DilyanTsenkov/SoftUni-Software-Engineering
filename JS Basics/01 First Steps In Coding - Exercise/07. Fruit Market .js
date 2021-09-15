function market(input1, input2, input3, input4, input5) {
    let strawberriesPrice = Number(input1)
    let banansKg = Number(input2)
    let orangesKg = Number(input3)
    let raspberriesKg = Number(input4)
    let strawberriesKg = Number(input5)
    let raspberriesPrice = strawberriesPrice / 2
    let orangesPrice = raspberriesPrice * 0.6
    let banansPrice = raspberriesPrice * 0.2
    let neededMoney = strawberriesPrice * strawberriesKg + raspberriesPrice * raspberriesKg + banansPrice * banansKg + orangesPrice * orangesKg
    console.log(neededMoney)
}
market("63.5", "3.57", "6.35", "8.15", "2.5")

