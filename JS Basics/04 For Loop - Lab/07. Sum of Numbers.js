function sumOfNum(n) {
    let sum = 0
    for (let i = 0; i < n.length; i++) {
        let character = n[i];
        sum += Number(character);
    }
    console.log(`The sum of the digits is:${sum}`);
}
sumOfNum("564891")  