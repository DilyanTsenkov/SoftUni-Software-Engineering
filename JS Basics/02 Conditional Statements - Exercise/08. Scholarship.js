function scholarship(salary, grade, minSalary) {
    grade = Number(grade);
    salary = Number(salary);
    minSalary = Number(minSalary);
    let social = 0
    let excellent = 0
    if ((salary < minSalary) & (grade > 4.5)) {
        social = minSalary * 0.35;
    }
    if (grade >= 5.50) {
        excellent = grade * 25;
    }
    if (social == 0 & excellent == 0) {
        console.log("You cannot get a scholarship!");
    }
    else if (social > excellent) {
        console.log(`You get a Social scholarship ${Math.floor(social)} BGN`);
    }
    else if (social <= excellent) {
        console.log(`You get a scholarship for excellent results ${Math.floor(excellent)} BGN`);
    }
}
scholarship("480.00","4.60","450.00")




