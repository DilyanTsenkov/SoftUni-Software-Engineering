function extractText() {
    let items = document.querySelectorAll("#items li");;
    let textArea = document.getElementById('result');
    for (let item of items) {
        textArea.value += item.textContent + '\n';
    }
}