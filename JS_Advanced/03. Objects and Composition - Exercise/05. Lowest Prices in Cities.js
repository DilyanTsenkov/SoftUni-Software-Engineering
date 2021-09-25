function lowerPrice(input) {
    let towns = []

    for (item of input) {
        let [townName, productName, productPrice] = item.split(' | ');
        let notFound = true;
        productPrice = Number(productPrice);
        let town = { 'townName': townName, 'productName': productName, 'productPrice': productPrice };
        if (towns.length == 0) {
            towns.push(town);
        }
        for (each of towns) {
            if (each.townName == town.townName && each.productName == town.productName) {
                each.productPrice = town.productPrice
                notFound = false;
                break;
            }
        }
        if (notFound) {
            towns.push(town);
        }
    }
    let checkedProduct = []
    for (item of towns) {
        let product = item.productName;
        let price = item.productPrice;
        let serchedTown = item.townName;
        if (checkedProduct.includes(product) != true) {
            checkedProduct.push(product);
            for (i of towns) {
                if (product == i.productName) {
                    if (i.productPrice < price) {
                        serchedTown = i.townName;
                        price = i.productPrice;
                    }
                }
            }
            console.log(`${product} -> ${price} (${serchedTown})`);
        }
    }
}

lowerPrice(['Sample Town | Sample Product | 1000',
    'Sample Town | Orange | 2',
    'Sample Town | Peach | 1',
    'Sofia | Orange | 3',
    'Sofia | Peach | 2',
    'New York | Sample Product | 1000.1',
    'New York | Burger | 10']
);

lowerPrice(['Sofia City | Audi | 100000',
    'Sofia City | BMW | 100000',
    'Sofia City | Mitsubishi | 10000',
    'Sofia City | Mercedes | 10000',
    'Sofia City | NoOffenseToCarLovers | 0',
    'Mexico City | Audi | 1000',
    'Mexico City | BMW | 99999',
    'New York City | Mitsubishi | 10000',
    'New York City | Mitsubishi | 1000',
    'Mexico City | Audi | 100000',
    'Washington City | Mercedes | 1000'
])