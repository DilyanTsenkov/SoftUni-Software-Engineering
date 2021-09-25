function car_factory(input) {
    let model = Object.keys(input)[0];
    let power = Object.keys(input)[1];
    let carriage = Object.keys(input)[2];
    let color = Object.keys(input)[3];

    let volume = 0;
    if (input.power <= 90) {
        input.power = 90;
        volume = 1800;
    } else if (90 < input.power && input.power <= 120) {
        input.power = 120;
        volume = 2400;
    } else if (120 < input.power) {
        input.power = 200;
        volume = 3500;
    };

    let whellSize = input.wheelsize;
    if (whellSize % 2 == 0) {
        whellSize -= 1;
    }
    let wheels = [0, 0, 0, 0];
    wheels.fill(whellSize);

    car = {
        model: input.model,
        "engine": { power: input.power, 'volume': volume },
        carriage: { 'type': input.carriage, color: input.color },
        "wheels": wheels
    };
    return (car);
}




car_factory({
    model: 'VW Golf II',
    power: 90,
    color: 'blue',
    carriage: 'hatchback',
    wheelsize: 14
}
)
car_factory({
    model: 'Opel Vectra',
    power: 200,
    color: 'grey',
    carriage: 'coupe',
    wheelsize: 17
}
);