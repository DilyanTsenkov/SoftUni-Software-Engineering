function diagonalAtack(matrix) {
    for (let row of matrix) {
        let element = (matrix.shift()).split(" ")
        matrix.push(element)
    }

    let row = 0;
    let col = 0;
    let mainDiagonal = 0;
    let secondDiagonal = 0;

    for (let i = 0; i < matrix.length; i++) {

        mainDiagonal += Number(matrix[row][col]);
        row += 1;
        col += 1;
    }

    row = 0;
    col = matrix.length - 1;
    for (let i = 0; i < matrix.length; i++) {
        secondDiagonal += Number(matrix[row][col]);
        row += 1;
        col -= 1;
    }
    let tempMatrix = [];
    if (mainDiagonal == secondDiagonal) {
        for (let i of matrix) {
            tempRow = i.map(function (num, n, arr) {
                return mainDiagonal;
            })
            tempMatrix.push(tempRow);

        }
        row = 0
        col = 0
        for (let i = 0; i < matrix.length; i++) {
            tempMatrix[row][col] = matrix[row][col];
            row += 1;
            col += 1;
        }
        row = 0;
        col = matrix.length - 1;
        for (let i = 0; i < matrix.length; i++) {
            tempMatrix[row][col] = matrix[row][col];
            row += 1;
            col -= 1;
        }
        for (let currentRow of tempMatrix) {
            console.log(currentRow.join(' '));
        }
    } else {
        for (let currentRow of matrix) {
            console.log(currentRow.join(' '));
        }
    }
}

diagonalAtack(['5 3 12 3 1', '11 4 23 2 5', '101 12 3 21 10', '1 4 5 2 2', '5 22 33 11 1']);
diagonalAtack(['1 1 1', '1 1 1', '1 1 0']);