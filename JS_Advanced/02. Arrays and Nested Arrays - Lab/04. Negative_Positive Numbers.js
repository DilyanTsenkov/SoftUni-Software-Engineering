function negativPositiveNum(input) {
    let result = [];
    for (let num of input) {
        if (num < 0) {
            result.unshift(num);
        } else { result.push(num) };
    }
    console.log(result.join("\n"));
}

negativPositiveNum([7, -2, 8, 9]);
negativPositiveNum([3, -2, 0, -1]);