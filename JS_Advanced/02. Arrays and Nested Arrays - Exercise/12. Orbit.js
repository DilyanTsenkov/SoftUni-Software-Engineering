function orbit(array) {
    let width = array[0];
    let height = array[1];
    let x = array[2];
    let y = array[3];

    let matrix = [];
    for (let r = 0; r < height; r++) {
        let tempRow = [];
        for (let c = 0; c < width; c++) {
            tempRow.push(0);
        }
        matrix.push(tempRow);
    }
    matrix[x][y] = 1
    for (let row = 0; row < height; row++) {
        for (let col = 0; col < width; col++) {
            matrix[row][col] = Math.max(Math.abs(row - x), Math.abs(col - y)) + 1;
        }
    }
    for (let row of matrix) {
        console.log(row.join(' '));
    }
}

orbit([4, 4, 0, 0]);
orbit([5, 5, 2, 2]);