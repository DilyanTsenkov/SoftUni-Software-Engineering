function listOfNames(names) {
    names.sort((a, b) => a.localeCompare(b));
    let currentNum = 1;
    for (let name of names) {
        console.log(`${currentNum}${'.'}${name}`)
        currentNum += 1;
    }
}

listOfNames(["John", "Bob", "Christina", "Ema"])