function convertor(number, inputDim, outputDim) {
    number = Number(number)
    let result = 0
    if ((inputDim === "mm") & (outputDim === "m")) {
        result = number / 1000;
    }
    else if ((inputDim === "mm") & (outputDim === "cm")) {
        result = number / 10;
    }
    else if ((inputDim === "mm") & (outputDim === "mm")) {
        result = number;
    }
    if ((inputDim === "cm") & (outputDim === "m")) {
        result = number / 100;
    }
    else if ((inputDim === "cm") & (outputDim === "mm")) {
        result = number * 10;
    }
    else if ((inputDim === "cm") & (outputDim === "cm")) {
        result = number;
    }
    if ((inputDim === "m") & (outputDim === "mm")) {
        result = number * 1000;
    }
    else if ((inputDim === "m") & (outputDim === "cm")) {
        result = number * 100;
    }
    else if ((inputDim === "m") & (outputDim === "m")) {
        result = number;
    }
    console.log(result.toFixed(3))
}
convertor("45", "cm", "mm")