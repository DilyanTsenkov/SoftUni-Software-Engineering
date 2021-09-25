function townsToJson(input) {
    let tabel = [];
    let firstRow = input.shift();
    firstRow = firstRow.slice(2, -2);
    let [col1, col2, col3] = firstRow.split(' | ');
    for (item of input) {
        let currentRow = item.slice(2, -2);
        let [town, latitude, longitude] = currentRow.split(' | ');
        latitude = Number(latitude);
        latitude=latitude.toFixed(2);
        latitude = Number(latitude);
        longitude = Number(longitude);
        longitude=longitude.toFixed(2);
        longitude = Number(longitude);

        let row={};
        row[col1] = town;
        row[col2] = latitude;
        row[col3] = longitude;
        tabel.push(row);
    }
    console.log(JSON.stringify(tabel));
}

townsToJson(['| Town | Latitude | Longitude |',
    '| Sofia | 42.696552 | 23.32601 |',
    '| Beijing | 39.913818 | 116.363625 |']
);
townsToJson(['| Town | Latitude | Longitude |',
    '| Veliko Turnovo | 43.0757 | 25.6172 |',
    '| Monatevideo | 34.50 | 56.11 |']
);