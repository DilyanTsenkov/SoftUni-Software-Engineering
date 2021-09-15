function area(b1, b2, h) {
    let sideB1 = Number(b1)
    let sideB2 = Number(b2)
    let hight = Number(h)
    let TrapezeArea = (sideB1 + sideB2) * hight / 2
    console.log(TrapezeArea.toFixed(2))
}
area(8, 13, 7)