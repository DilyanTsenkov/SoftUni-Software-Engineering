function aqua(input1, input2, input3, input4) {
    let length = Number(input1)
    let width = Number(input2)
    let hight = Number(input3)
    let percent = Number(input4)
    let full = length * width * hight
    let water = full * (100 - percent) / 100000
    console.log(water)
}
aqua("105", "77", "89", "18.5")

