function mathOperator(num1, num2, sign) {
    let result;
    switch (sign) {
        case '+': result = num1 + num2; break;
        case '-': result = num1 - num2; break;
        case '*': result = num1 * num2; break;
        case '/': result = num1 / num2; break;
        case '%': result = num1 % num2; break;
        case '**': result = num1 ** num2; break;
    }
    console.log(result);
}

mathOperator(5, 6, '+')
mathOperator(3, 5.5, '*')