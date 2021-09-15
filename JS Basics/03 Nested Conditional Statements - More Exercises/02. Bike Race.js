function race(juniors, seniors, trace) {
    juniors = Number(juniors);
    seniors = Number(seniors);
    let taxJuniors = 0;
    let taxSeniors = 0;
    switch (trace) {
        case "trail":
            taxJuniors = 5.50 * juniors;
            taxSeniors = 7 * seniors;
            break;
        case "cross-country":
            taxJuniors = 8 * juniors;
            taxSeniors = 9.5 * seniors;
            if ((juniors + seniors) >= 50) {
                taxJuniors *= 0.75;
                taxSeniors *= 0.75;
            }
            break;
        case "downhill":
            taxJuniors = 12.25 * juniors;
            taxSeniors = 13.75 * seniors;
            break;
        case "road":
            taxJuniors = 20 * juniors;
            taxSeniors = 21.50 * seniors;
            break;
    }
    let donation = (taxSeniors + taxJuniors) * 0.95;
    console.log(donation.toFixed(2))

}
race(3, 40, "road")