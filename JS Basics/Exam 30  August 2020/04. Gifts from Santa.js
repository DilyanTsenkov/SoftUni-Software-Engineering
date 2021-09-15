function santa(n, m, s) {
    n = Number(n);
    m = Number(m);
    s = Number(s);
    let print = [];
    for (let i = m; i >= n; i--) {
        if (i % 2 == 0 && i % 3 == 0) {
            if (i == s) {
                break;
            }
            print.push(i);
        }
    }
    console.log(print.join(" "));
}
santa("1", "36", "12")