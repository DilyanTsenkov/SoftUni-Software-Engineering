function pyramid(input) {
    let n = input[0];
    let number = 0;
    let rowNumbers = [];
    let deleteCount = 0
    for (let row = 1; row <= n; row++) {
        for (let col = 1; col <= row; col++) {
            number++;
            if (n < number) {
                break;
            }
            rowNumbers.push(number);
        }
        rowNumbers.splice(0, deleteCount);
        console.log(rowNumbers.join(" "));
        deleteCount++;
        if (n < number) {
            break;
        }
    }
}
pyramid(["0"])