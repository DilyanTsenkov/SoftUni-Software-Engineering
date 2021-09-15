function log(input) {
    let username = input[0];
    let password = input[1];
    let index = 2;
    while (true) {
        let pass = input[index];
        index++;
        if (pass == password) {
            console.log(`Welcome ${username}!`);
            break;
        }
    }
}
log(["Gosho",
    "secret",
    "secret"])

