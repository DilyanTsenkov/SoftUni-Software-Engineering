function data(name, lastname, age, town) {
    let fname = name
    let lname = lastname
    let a = Number(age)
    let t = town
    console.log(`You are ${fname} ${lname}, a ${a}-years old person from ${t}.`)
}
data("Maria", "Petrova", 20, "Plovdiv")