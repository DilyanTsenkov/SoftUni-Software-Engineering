function gcd(x, y) {
    while (y) {
        let temp = y;
        y = x % y;
        x = temp;
    }
    console.log(x);
}

gcd(2154, 458)