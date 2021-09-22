function lastK(arg1, arg2) {
    let array = [1]
    for (let i = 1; i < arg1; i++) {
        let new_arg = array.slice(Math.max(0, i - arg2), i).reduce((a, b) => a + b);
        array.push(new_arg);
    }
    return array;
}

lastK(6, 3)
lastK(8, 2)