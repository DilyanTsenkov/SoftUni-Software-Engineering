function numbers(n) {
    n = Number(n);
    for (let i = 0; i <= n; i += 2) {
        console.log(2 ** i);
    }
}
numbers("6")