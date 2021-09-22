function rotation(array, number) {
    let currentElement;
    for (let i = 0; i < number; i++) {
        currentElement = array.pop();
        array.unshift(currentElement);
    }
    console.log(array.join(' '));
}

rotation(['1',
    '2',
    '3',
    '4'],
    2
);

rotation(['Banana',
    'Orange',
    'Coconut',
    'Apple'],
    15
)