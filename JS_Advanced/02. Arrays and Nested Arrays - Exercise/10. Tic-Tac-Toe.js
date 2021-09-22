function ticTacToe(moves) {
    let field = [[false, false, false],
    [false, false, false],
    [false, false, false]]

    for (let m = 0; m < moves.length; m++) {
        if (m % 2 == 0) {
            let move = moves[m][0]
            if (move == false) {
                field[move[0]][move[1]] = "x";
            } else {
                move = moves[m[0]][m[1]]
                if (move == false) {
                    moves[m[0]][m[1]] = "O";
                }
            }
        }

    }
}
ticTacToe(["0 0",
    "0 0",
    "1 1",
    "0 1",
    "1 2",
    "0 2",
    "2 2",
    "1 2",
    "2 2",
    "2 1"]
)