function rectangle(count) {
    let array = [];
    if (count == 1) {
        console.log('*');
    } else {
        for (let i = 0; i < count; i++) {
            for (let i = 0; i < count; i++) {
                array.push("*");
            }
            console.log(array.join(' '));
            array = [];
        }
    }
}

rectangle(5)