function counter(message) {
    let spaceCounter = 0;
    for (let i = 0; i <= message.length; i++) {
        if (message[i] == " ") {
            spaceCounter += 1;
        }
    }
    if (spaceCounter > 9) {
        console.log(`The message is too long to be send! Has ${spaceCounter + 1} words.`);
    }
    else {
        console.log(`The message was send successfully!`);
    }
}
counter("This message has ten words and you can send it!")