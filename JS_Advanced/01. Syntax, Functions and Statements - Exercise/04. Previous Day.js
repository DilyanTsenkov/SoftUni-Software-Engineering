function previousDate (y,m,d){
    let date = new Date(y,m-1,d);
    date.setDate(date.getDate() - 1);
    console.log(date.getFullYear() +  "-" + (date.getMonth()+1) + "-" + date.getDate());
}

previousDate(2016, 9, 30)
previousDate(2016, 10, 1)