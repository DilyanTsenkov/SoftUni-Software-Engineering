function logistic(numbers) {
    let n = Number(numbers[0]);
    let busTransport = 0;
    let truckTransport = 0;
    let trainTransport = 0;
    let price = 0;
    let tones = 0;
    for (let i = 1; i <= n; i++) {
        let load = Number(numbers[i]);
        if (load <= 3) {
            busTransport += load;
            price += load * 200;
            tones += load;
        }
        else if (4 <= load && load <= 11) {
            truckTransport += load;
            price += load * 175;
            tones += load;
        }
        else {
            trainTransport += load;
            price += load * 120;
            tones += load;
        }
    }
    let averagePrice = price / tones;
    let percentBusTransport = busTransport / tones * 100;
    let percentTruckTransport = truckTransport / tones * 100;
    let percentTrainTransport = trainTransport / tones * 100;
    console.log(averagePrice.toFixed(2));
    console.log(`${percentBusTransport.toFixed(2)}%`);
    console.log(`${percentTruckTransport.toFixed(2)}%`);
    console.log(`${percentTrainTransport.toFixed(2)}%`);
}
logistic([5, 2, 10, 20, 1, 7])