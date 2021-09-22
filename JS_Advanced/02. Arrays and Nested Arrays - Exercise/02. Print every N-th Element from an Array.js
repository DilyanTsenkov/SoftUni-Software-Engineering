function printer(array, number) {
    let result = [];
    for (let i = 0; i < array.length; i += number) {
        result.push(array[i]);
        }
    return result;
}

printer(['5',
    '20',
    '31',
    '4',
    '20'],
    2
);
printer(['dsa',
    'asd',
    'test',
    'tset'],
    2
);
printer(['1',
    '2',
    '3',
    '4',
    '5'],
    3
);
