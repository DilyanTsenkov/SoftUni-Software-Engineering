def pieces(pieces):
    db_pieces = {}
    for p in range(pieces):
        piece, composer, key = input().split("|")
        db_pieces[piece] = {"composer": composer, "key": key}
    return db_pieces


def add(my_pieces, piece, composer, key):
    if piece in my_pieces:
        print(f"{piece} is already in the collection!")
    else:
        my_pieces[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    return my_pieces


def remove(my_pieces, piece):
    if piece in my_pieces:
        my_pieces.pop(piece)
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return my_pieces


def change_key(my_pieces, piece, key):
    if piece in my_pieces:
        my_pieces[piece]["key"] = key
        print(f"Changed the key of {piece} to {key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return my_pieces


pieces_count = int(input())
my_pieces = pieces(pieces_count)

while True:
    command = input()
    if command == "Stop":
        break
    command = command.split("|")
    action = command[0]
    piece_name = command[1]
    if action == "Add":
        my_pieces = add(my_pieces, piece_name, command[2], command[3])
    elif action == "Remove":
        my_pieces = remove(my_pieces, piece_name)
    elif action == "ChangeKey":

        my_pieces = change_key(my_pieces, piece_name, command[2])
my_pieces = dict(sorted(my_pieces.items(), key=lambda x: (x[0], x[1]["composer"])))

for key, value in my_pieces.items():
    print(f'{key} -> Composer: {value["composer"]}, Key: {value["key"]}')
