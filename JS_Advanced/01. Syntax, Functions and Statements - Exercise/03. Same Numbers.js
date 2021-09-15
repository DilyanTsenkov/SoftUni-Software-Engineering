function same(number) {
    let sum = 0;
    let length = String(number).length

    for (let i = 0; i < length; i++) {
        let tempNum = String(number)[i];
        sum += Number(tempNum);
    }

    let flag = true;
    let firstNum = String(number)[0];
    for (let i = 1; i < length; i++) {
        let currentNum = String(number)[i];
        if (Number(firstNum) != Number(currentNum)) {
            flag = false;
            break;
        }
    }
    console.log(flag);
    console.log(sum);
}

same(322222)