function colorize() {
    let tableRows = document.querySelectorAll("table tr");
    // let tableRows = document.getElementsByTagName("tr"); #another way to select 
    for (let i = 1; i < tableRows.length; i += 2) {
        tableRows[i].style.backgroundColor = 'teal';
    }
}
