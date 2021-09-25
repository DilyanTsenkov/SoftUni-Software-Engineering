function heroRegister(heroes) {
    let listOfHeroes = [];
    for (let i = 0; i < heroes.length; i++) {
        let [heroName, heroLevel, heroItems] = heroes[i].split(' / ');
        heroLevel = Number(heroLevel);
        if (heroItems) {
            heroItems = heroItems.split(", ");
        } else {
            heroItems = [];
        }
        let hero = { 'name': heroName, 'level': heroLevel, 'items': heroItems };
        listOfHeroes.push(hero);
    }
    console.log(JSON.stringify(listOfHeroes));
}

heroRegister(['Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara']
);
heroRegister(['Jake / 1000 / Gauss, HolidayGrenade']);