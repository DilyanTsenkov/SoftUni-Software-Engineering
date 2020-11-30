cards = input().split(" ")
shuffles = int(input())

new_card_list_print = []
new_card_list = []
slice_place = int(len(cards) / 2)
first_half_cards_list = cards[:slice_place]
second_half_cards_list = cards[slice_place:]

for shuffle in range(shuffles):

    for card in range(slice_place):
        new_card_list.append(first_half_cards_list[card])
        new_card_list.append(second_half_cards_list[card])

    first_half_cards_list = new_card_list[:slice_place]
    second_half_cards_list = new_card_list[slice_place:]
    new_card_list_print = new_card_list
    new_card_list = []

print(new_card_list_print)
