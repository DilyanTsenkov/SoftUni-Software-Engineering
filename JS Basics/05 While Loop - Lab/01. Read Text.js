function read(input) {
    let index = 0;
    while (true) {
        let text = input[index];
        index++;
        if (text == "Stop") {
            break;
        }
        console.log(text);
    }
}
read(["Sofia",
    "Berlin",
    "Moscow",
    "Athens",
    "Madrid",
    "London",
    "Paris",
    "Stop",
    "AfterStop"])

