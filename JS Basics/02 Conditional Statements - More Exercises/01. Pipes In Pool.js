function pool(volume, P1, P2, H) {
    volume = Number(volume);
    let volumePipe1 = Number(P1) * Number(H);
    let volumePipe2 = Number(P2) * Number(H);
    let totalVolume = volumePipe1 + volumePipe2;
    let percentPipe1 = volumePipe1 / totalVolume * 100;
    let percentPipe2 = volumePipe2 / totalVolume * 100;
    let percentTotal = totalVolume / volume * 100;
    if (volume >= volumePipe1 + volumePipe2) {
        console.log(`The pool is ${(percentTotal).toFixed(2)}% full.Pipe 1: ${percentPipe1.toFixed(2)}%.Pipe 2: ${percentPipe2.toFixed(2)}%.`);
    }
    else {
        console.log(`For ${H} hours the pool overflows with ${(volumePipe2 + volumePipe1 - volume).toFixed(2)} liters.`);
    }
}
pool(100, 100, 100, 2.5)