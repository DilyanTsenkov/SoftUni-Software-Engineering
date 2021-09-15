function invalid(number) {
    number = Number(number);
    if ((100 > number || number > 200) && (number != 0)) {
        console.log("invalid");
    }
}
invalid("0")