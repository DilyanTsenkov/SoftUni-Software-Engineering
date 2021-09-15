function zoo(dogs, animals) {
    let dog_count = Number(dogs)
    let animal_count = Number(animals)
    let food = dog_count * 2.5 + animal_count * 4
    console.log(`${food} lv`)
}
zoo("13", "9")