function table() {
    for (let i = 1; i <= 10; i++) {
        for (let n = 1; n <= 10; n++) {
            let sum = i * n;
            console.log(`${i} * ${n} = ${sum}`);
        }
    }
}
table()