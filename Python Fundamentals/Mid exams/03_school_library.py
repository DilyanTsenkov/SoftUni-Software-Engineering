book_names = input().split("&")

while True:
    command = input().split(" | ")
    if command[0] == "Done":
        break

    if command[0] == "Add Book":
        if command[1] not in book_names:
            book_names.insert(0, command[1])

    elif command[0] == "Take Book":
        if command[1] in book_names:
            book_names = [book for book in book_names if book != command[1]]

    elif command[0] == "Swap Books":
        if command[1] in book_names and command[2] in book_names:
            book1_index = book_names.index(command[1])
            book2_index = book_names.index(command[2])
            book_names[book1_index], book_names[book2_index] = book_names[book2_index], book_names[book1_index]

    elif command[0] == "Insert Book":
        book_names.append(command[1])

    elif command[0] == "Check Book":
        if int(command[1]) in range(len(book_names)):
            print(book_names[int(command[1])])

print(", ".join(book_names))
