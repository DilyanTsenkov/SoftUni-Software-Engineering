function hall(input1, input2) {
    let widht = Number(input2)
    let length = Number(input1)
    let widthPlaces = (widht - 1) / 0.7
    let lengthPlaces = length / 1.2
    let allPlaces = Math.floor(widthPlaces) * Math.floor(lengthPlaces) - 3
    console.log(allPlaces)
}
hall(15, 8.9)