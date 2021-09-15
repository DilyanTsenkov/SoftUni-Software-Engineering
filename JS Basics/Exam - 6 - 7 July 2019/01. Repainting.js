function painting(naylon, paint, thinner, hours) {
    let materials = Number(naylon) * 1.5 + Number(paint) * 14.5 + Number(thinner) * 5;
    let addMaterials = 0.1 * Number(paint) * 14.5 + 2 * 1.5 + 0.4;
    let allMaterials = materials + addMaterials;
    let work = Number(hours) * allMaterials * 0.3;
    let costs = allMaterials + work;
    console.log(`Total expenses: ${costs.toFixed(2)} lv.`);
}
painting(90, 99, 28, 9)
