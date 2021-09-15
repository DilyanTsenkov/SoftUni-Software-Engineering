function agesex(age, sex) {
    age = Number(age);
    if (age >= 16) {
        if (sex == "m") {
            console.log("Mr.");
        }
        else {
            console.log("Ms.");
        }
    }
    else {
        if (sex == "m") {
            console.log("Master");
        }
        else {
            console.log("Miss");
        }
    }
}
agesex("13.5", "m")



