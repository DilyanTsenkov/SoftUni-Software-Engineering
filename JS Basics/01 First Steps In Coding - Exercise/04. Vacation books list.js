function reading(input1, input2, input3) {
    let pages = Number(input1)
    let pagesPerHour = Number(input2)
    let days = Number(input3)
    let bookReadingHours = pages / pagesPerHour
    let DayReadingTime = bookReadingHours / days
    console.log(DayReadingTime)
}
reading("432", "15", "4")

