function clock() {
    for (let hour = 0; hour <= 23; hour++) {
        for (let minute = 0; minute <= 59; minute++) {
            for (let seconds = 0; seconds <= 59; seconds++) {
                console.log(`${hour} : ${minute} : ${seconds}`);
            }
        }
    }
}