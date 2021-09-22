function magicChecker(matrix) {
    let flag = true;
    let reducer = (accumulator, currentValue) => accumulator + currentValue;
    let firstRow = matrix[0];
    let firstRowSum = firstRow.reduce(reducer);
    for (let row of matrix) {
        let currentRowSum = row.reduce(reducer)
        if (currentRowSum != firstRowSum) {
            flag = false;
            break;
        }
    }

    let firstCol = 0;
    for (let i = 0; i < matrix.length; i++) {
        firstCol += matrix[i][0];
    }
    for (let col = 0; col < matrix[0].length; col++) {
        let currentCol = 0;
        for (let row = 0; row < matrix.length; row++) {
            currentCol += matrix[row][col]
        }
        if (firstCol != currentCol) {
            flag = false;
            break;
        }
    }
    return flag;
}

magicChecker([[4, 5, 6], [6, 5, 4], [5, 5, 5]]);
magicChecker([[11, 32, 45], [21, 0, 1], [21, 1, 1]]);
magicChecker([[1, 0, 0], [0, 0, 1], [0, 1, 0]]);

