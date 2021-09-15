function cooking() {
    let array = Array.from(arguments);
    let number = Number(array.shift());

    while (array.length > 0) {
        let command = array.shift();
        switch (command) {
            case 'chop': number /= 2; break;
            case 'dice': number = Math.sqrt(number); break;
            case 'spice': number += 1; break;
            case 'bake': number *= 3; break;
            case 'fillet': number *= 0.8; break;
        }
        console.log(number);
    }
}
cooking('32', 'chop', 'chop', 'chop', 'chop', 'chop')
cooking('9', 'dice', 'spice', 'chop', 'bake', 'fillet')