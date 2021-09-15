function threeStrings(a, b, c) {
    let length = a.length + b.length + c.length;
    let average = Math.floor(length / 3);
    console.log(length);
    console.log(average);
}

threeStrings('chocolate', 'ice cream', 'cake')
threeStrings('pasta', '5', '22.3')