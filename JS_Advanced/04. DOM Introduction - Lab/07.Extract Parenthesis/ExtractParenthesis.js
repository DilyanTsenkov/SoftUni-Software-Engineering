function extract(content) {
    let paragraph = document.getElementById(content).textContent;
    let regPattern = /\(([^)]+)\)/g;
    let result = [];

    let match = regPattern.exec(paragraph);
    while (match) {
        result.push(match[1]);
        match = regPattern.exec(paragraph);
    }
    return result.join('; ');
}

