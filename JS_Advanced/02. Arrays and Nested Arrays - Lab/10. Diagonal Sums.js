function diagonalSum(matrix) {
    let row = 0;
    let col = 0;
    let mainDiagonal = 0;
    let secondDiagonal = 0;

    for (let i = 0; i < matrix.length; i++) {
        mainDiagonal += matrix[row][col];
        row += 1;
        col += 1;
    }

    row = 0;
    col = matrix.length - 1;
    for (let i = 0; i < matrix.length; i++) {
        secondDiagonal += matrix[row][col];
        row += 1;
        col -= 1;
    }

    console.log(mainDiagonal, secondDiagonal);
}

diagonalSum([[20, 40],
[10, 60]]
);
diagonalSum([[3, 5, 17],
[-1, 7, 14],
[1, -8, 89]]
);