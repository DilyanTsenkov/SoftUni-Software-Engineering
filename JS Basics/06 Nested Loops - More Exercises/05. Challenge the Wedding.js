function challenge(input) {
    let men = Number(input[0]);
    let women = Number(input[1]);
    let places = Number(input[2]);
    let print = "";
    let counter = 0;
    let noPlaces = false;
    for (let man = 1; man <= men; man++) {
        for (let woman = 1; woman <= women; woman++) {
            counter++;
            print += `(${man} <-> ${woman}) `;
            if (counter == places) {
                noPlaces = true;
                break;
            }
        }

        if (noPlaces == true) {
            break;
        }
    }
    console.log(print);
}
challenge([5, 8, 40])
