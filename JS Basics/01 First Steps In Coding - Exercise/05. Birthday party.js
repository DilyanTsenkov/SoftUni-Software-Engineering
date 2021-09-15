function birthday(input) {
    let rent = Number(input)
    let cake = rent * 0.2
    let drinks = cake * 0.55
    let animator = rent / 3
    let budget = cake + drinks + animator + rent
    console.log(budget)
}
birthday("3720")