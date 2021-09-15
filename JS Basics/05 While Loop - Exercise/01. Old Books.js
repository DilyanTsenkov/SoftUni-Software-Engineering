function library(input) {
    let aniBook = input[0];
    let index = 1;
    let counter = 0;
    let found = false;
    while (true) {
        let book = input[index];
        index++;
        if (book == aniBook) {
            console.log(`You checked ${counter} books and found it.`);
            found = true;
            break;
        }
        if (book == "No More Books") {
            break;
        }
        counter += 1
    }
    if (found == false) {
        console.log(`The book you search is not here!`);
        console.log(`You checked ${counter} books.`);
    }
}
library(["Bourne",
    "True Story",
    "Forever",
    "More Space",
    "The Girl",
    "Spaceship",
    "Strongest",
    "Profit",
    "Tripple",
    "Stella",
    "The Matrix",
    "Bourne"])


