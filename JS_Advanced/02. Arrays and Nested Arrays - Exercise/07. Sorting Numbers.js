function sortingNumbers(numbers) {
    numbers.sort((a, b) => a - b);
    let result = [];

    while (numbers.length > 0) {
        let element = numbers.shift();
        result.push(element);
        element = numbers.pop();
        result.push(element);
    }
    return result;
}

sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56])