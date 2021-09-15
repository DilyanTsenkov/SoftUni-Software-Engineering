function convertor(input) {
    let rad = Number(input);
    let dgr = rad * 180 / Math.PI;
    console.log(dgr.toFixed(0));
}
convertor("6.2832")