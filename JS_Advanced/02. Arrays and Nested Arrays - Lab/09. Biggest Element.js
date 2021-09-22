function bigestFinder(input) {
    let bigest = -100000000000000000000
    for (let r = 0; r < input.length; r++) {
        for (let c = 0; c < input[r].length; c++) {
            if (input[r][c] > bigest) {
                bigest = input[r][c];
            }
        }
    }
    return bigest;
}

bigestFinder([[20, 50, 10],
[8, 33, 145]])
bigestFinder([[3, 5, 7, 12],
[-1, 4, 33, 2],
[8, 3, 0, 4]]
)
