function extractor(array) {
    let bigest = array[0];
    let result = [];
    for (let num of array) {
        if (num >= bigest) {
            result.push(num);
            bigest = num;
        }
    }
    return result;
}

extractor([1, 3, 8, 4, 10, 12, 3, 2, 24]);
extractor([1, 2, 3, 4]);
extractor([20, 3, 2, 15, 6, 1])