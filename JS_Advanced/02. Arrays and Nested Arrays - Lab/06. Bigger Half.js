function biggerHalf(input) {
    let searchingHalf = Math.floor(input.length / 2);
    input.sort((a, b) => a - b);
    let result = input.slice(searchingHalf, input.length);
    return result;
}

biggerHalf([4, 7, 2, 5]);
biggerHalf([3, 19, 14, 7, 2, 19, 6]);