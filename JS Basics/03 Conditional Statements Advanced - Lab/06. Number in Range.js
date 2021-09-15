function interval(number) {
    number = Number(number);
    if (-100 <= number && number <= 100 && number != 0) {
        console.log("Yes");
    }
    else {
        console.log("No");
    }
}
interval(0)