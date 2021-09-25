function sumTable() {
    let tableRows = document.querySelectorAll('table tr');
    let tableSum = document.getElementById('sum');
    let sum = 0;
    for (let i = 1; i < tableRows.length - 1; i++) {
        let number = tableRows[i].lastElementChild.textContent;
        sum += Number(number);
    }
    tableSum.textContent = sum;
}