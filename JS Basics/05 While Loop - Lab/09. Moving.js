function noWayHose(input) {
    let width = Number(input[0]);
    let length = Number(input[1]);
    let high = Number(input[2]);
    let index = 3;
    let freespace = width * length * high;
    while (true) {
        let box = input[index];
        index++;
        if (box == "Done") {
            console.log(`${freespace} Cubic meters left.`);
            break;
        }
        freespace -= Number(box);
        if (freespace < 0) {
            console.log(`No more free space! You need ${freespace * -1} Cubic meters more.`);
            break;
        }
    }
}
noWayHose(["10",
"1",
"2",
"4",
"6",
"Done"])






