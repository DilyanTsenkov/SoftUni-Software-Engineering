function firstLastSum(input) {
    let first = Number(input[0]);
    let length = input.length;
    let last = Number(input[length - 1]);
    let sum = first + last;
    console.log(sum);
}

firstLastSum(['20', '30', '40']);
firstLastSum(['5', '10']);