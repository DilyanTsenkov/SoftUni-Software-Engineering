function sorting(products) {
    let catalogue = [];
    for (let product of products) {
        let [name, price] = product.split(' : ');
        price = Number(price);
        let item = { name, price };
        catalogue.push(item);
    }
    catalogue.sort(function (a, b) {
        return a.name.localeCompare(b.name)
    });
    let catalogArray = []
    for (let l = 65; l <= 90; l++) {
        let letter = String.fromCharCode(l)
        let catalogObjects = { letter, content: [] }
        for (i of catalogue) {
            if (i.name[0] == letter) {
                catalogObjects.content.push(i)
            }
        }
        catalogArray.push(catalogObjects)
    }
    for (object of catalogArray) {
        if (object.content.length > 0) {
            console.log(object.letter);
            for (o of object.content) {
                console.log(`${o.name}: ${o.price}`)
            }
        }
    }
}





sorting(['Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10']
);
sorting(['Banana : 2',
    'Rubic`s Cube : 5',
    'Raspberry P : 4999',
    'Rolex : 100000',
    'Rollon : 10',
    'Rali Car : 2000000',
    'Pesho : 0.000001',
    'Barrel : 10']
)