function addOrRemove(commands) {
    let number = 1;
    let result = [];
    for (let command of commands) {
        if (command == 'add') {
            result.push(number);
        } else {
            result.pop();
        }
        number += 1;
    };
    if (result.length == 0) {
        console.log('Empty');
    } else {
        console.log(result.join('\n'));
    }
}

addOrRemove(['add',
    'add',
    'add',
    'add']
);

addOrRemove(['add',
    'add',
    'remove',
    'add',
    'add']
);

addOrRemove(['remove',
    'remove',
    'remove']
)