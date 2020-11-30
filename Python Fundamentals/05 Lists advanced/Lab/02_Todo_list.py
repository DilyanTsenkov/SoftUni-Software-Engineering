todo_notes = input().split("-")

list_todo_notes = [0 for _ in range(10)]

while todo_notes[0] != "End":
    list_todo_notes.pop(int(todo_notes[0])-1)
    list_todo_notes.insert(int(todo_notes[0])-1, todo_notes[1])

    todo_notes = input().split("-")

list_todo_notes = [el for el in list_todo_notes if el != 0]

print(list_todo_notes)
