function cityRecord(name, population, treasury) {
    let result = {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += this.population * this.taxRate;
        },
        applyGrowth(percent) {
            this.population += Math.floor(this.population * percent / 100);
        },
        applyRecession(percent) {
            this.treasury -= Math.ceil(this.treasury * percent / 100);
        }
    };
    return result;
}

const city = cityRecord('Tortuga',7000,15000);
console.log(city);
city.collectTaxes();
console.log(city);
city.applyGrowth(5);
console.log(city);
