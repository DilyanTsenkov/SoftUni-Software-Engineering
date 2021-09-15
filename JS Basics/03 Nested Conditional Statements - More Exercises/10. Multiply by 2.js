let number = 0
    while (input >= 0) {
        number = input[index]
        if (number >= 0) {
            console.log(`Result: ${(number * 2).toFixed(2)}`)
        }
        else {
            console.log("Negative number!")
        }
    }

num([12, 43.2144, 12.3, 543.23, -20])