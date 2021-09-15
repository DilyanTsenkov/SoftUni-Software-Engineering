function bills(input) {
    let months = Number(input[0]);
    let water = 20 * months;
    let internet = 15 * months;
    let other = 0
    let electricity = 0
    for (let i = 1; i <= months; i++) {
        let electricityPerMonth = Number(input[i]);
        other += (20 + 15 + electricityPerMonth) * 1.2;
        electricity += electricityPerMonth;
    }
    let avrPerMonth = (water + internet + electricity + other) / months;
    console.log(`Electricity: ${electricity.toFixed(2)} lv`);
    console.log(`Water: ${water.toFixed(2)} lv`);
    console.log(`Internet: ${internet.toFixed(2)} lv`);
    console.log(`Other: ${other.toFixed(2)} lv`);
    console.log(`Average: ${avrPerMonth.toFixed(2)} lv`);
}
bills([8, 123.54, 231.54, 140.23, 100, 122.4, 430, 178.52, 64.2])