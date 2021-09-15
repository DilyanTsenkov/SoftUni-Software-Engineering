function uppercase(string) {
    let uppercaseString = string.toUpperCase();
    let results = uppercaseString.match(/[\w]+|\"[\w\s]+\"/g);
    console.log(results.join(", "));
}

uppercase('Hi, how are you?')
uppercase('hello')