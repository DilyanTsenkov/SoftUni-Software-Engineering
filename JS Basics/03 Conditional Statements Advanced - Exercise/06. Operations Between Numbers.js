function operation(n1, n2, operator) {
    n1 = Number(n1);
    n2 = Number(n2);
    let result = 0
    let evenOdd = "odd"
    switch (operator) {
        case "+":
            result = n1 + n2;
            if (result % 2 == 0) {
                evenOdd = "even"
            }
            console.log(`${n1} ${operator} ${n2} = ${result} - ${evenOdd}`);
            break;
        case "-":
            result = n1 - n2;
            if (result % 2 == 0) {
                evenOdd = "even"
            }
            console.log(`${n1} ${operator} ${n2} = ${result} - ${evenOdd}`);
            break;
        case "*":
            result = n1 * n2;
            if (result % 2 == 0) {
                evenOdd = "even"
            }
            console.log(`${n1} ${operator} ${n2} = ${result} - ${evenOdd}`);
            break;
        case "/":
            if (n2 == 0) {
                console.log(`Cannot divide ${n1} by zero`);
            }
            else {
                result = n1 / n2;
                console.log(`${n1} ${operator} ${n2} = ${result.toFixed(2)}`);
            }
            break;
        case "%":
            if (n2 == 0) {
                console.log(`Cannot divide ${n1} by zero`);
            }
            else {
                result = n1 % n2;
                console.log(`${n1} ${operator} ${n2} = ${result}`);
            }
            break;
    }
}
operation("7","3","*")







