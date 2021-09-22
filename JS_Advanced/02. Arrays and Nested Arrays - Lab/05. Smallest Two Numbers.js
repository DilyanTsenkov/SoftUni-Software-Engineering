function smalles(input) {
    input.sort((a, b) => a - b);
    console.log(input[0] + " " + input[1]);
}

smalles([30, 15, 50, 5]);
smalles([3, 0, 10, 4, 7, 3]);