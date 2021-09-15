function project(arh, projects) {
    let arh_name = arh
    let project_count = Number(projects)
    let time = project_count * 3
    console.log(`The architect ${arh_name} will need ${time} hours to complete ${project_count} project/s.`)
}
project("Sanya", "9")

