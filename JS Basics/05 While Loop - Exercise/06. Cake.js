function birthday(input) {
    let width = Number(input[0]);
    let length = Number(input[1]);
    let cake = width * length;
    let index = 2;
    let counter = 0;
    while (true) {
        let pieces = input[index];
        index++;
        if (pieces == "STOP") {
            console.log(`${cake} pieces are left.`);
            break;
        }
        counter = Number(pieces)
        cake -= counter;
        if (cake <= 0) {
            console.log(`No more cake left! You need ${Math.abs(cake)} pieces more.`);
            break;
        }
    }
}
birthday(["10",
    "2",
    "2",
    "4",
    "6",
    "STOP"])

