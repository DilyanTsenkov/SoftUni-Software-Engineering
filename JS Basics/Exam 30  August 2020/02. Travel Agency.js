function stamat(tickets, budget, ticketPrice) {
    ticketPrice = Number(ticketPrice);
    budget = Number(budget);
    tickets = Number(tickets);
    let neededmoney = ticketPrice * tickets;
    let change = budget - neededmoney
    if (budget < neededmoney) {
        console.log(`The budget of ${budget}$ is not enough. Your client can't buy ${tickets} tickets with this budget!`);
    }
    else {
        console.log(`You can sell your client ${tickets} tickets for the price of ${neededmoney}$!`);
        console.log(`Your client should become a change of ${change}$!`);
    }
}
stamat("3", "800", "300")