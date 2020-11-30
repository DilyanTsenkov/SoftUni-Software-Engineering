event_list_up = []
event_list_low = []

while True:
    event = input()
    if event == "END":
        break
    elif event == "coding" or event == "dog" or event == "cat" or event == "movie" or event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        if (event[0].isupper()) == True:
            event_list_up.append(event)
        else:
            event_list_low.append(event)
coffee = len(event_list_up) * 2 + len(event_list_low)
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
