function createObject(input) {
    object = {};
    for (let i = 0; i < input.length; i += 2) {
        let key = input[i];
        let value = Number(input[i + 1]);
        object[key] = value;
    }
    console.log(object);
}
createObject(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']);
createObject(['Potato', '93', 'Skyr', '63', 'Cucumber', '18', 'Milk', '42']);