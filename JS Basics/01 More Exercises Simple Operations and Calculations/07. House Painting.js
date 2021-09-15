function painting(x, y, h) {
    let hight = Number(x)
    let length = Number(y)
    let roofHight = Number(h)
    let rearWall = hight * hight
    let sideWall = length * hight - 1.5 * 1.5
    let roof = 2 * hight * length + 2 * hight * roofHight / 2
    let greenPaint = ((2 * rearWall - 1.2 * 2) + 2 * sideWall) / 3.4
    let redPaint = roof / 4.3
    console.log(greenPaint.toFixed(2))
    console.log(redPaint.toFixed(2))
}
painting(10.25, 15.45, 8.88)