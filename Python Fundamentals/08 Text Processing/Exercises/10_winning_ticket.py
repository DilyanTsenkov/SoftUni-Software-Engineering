def validator(ticket_checker):
    if len(ticket_checker) != 20:
        return False
    return True


def winner_searcher(part, win_symbol):
    counter = 0
    symbol_counter = 0
    p_symbol = ""
    symbol = ""
    for n in range(10):
        current_symbol = part[n]
        if current_symbol == p_symbol and current_symbol in win_symbol:
            counter += 1
            if counter >= 6:
                symbol = current_symbol
                symbol_counter = counter
        elif current_symbol in win_symbol:
            p_symbol = current_symbol
            counter = 1
        else:
            counter = 0
            p_symbol = current_symbol
    return symbol, symbol_counter


tickets = input().split(", ")
winners = ["@", "#", "$", "^"]

for ticket in tickets:
    ticket = ticket.strip()
    is_valid = validator(ticket)
    if not is_valid:
        print("invalid ticket")
    else:
        first_part_symbol, first_part_counter = winner_searcher(ticket[:10], winners)
        second_part_symbol, second_part_counter = winner_searcher(ticket[10:], winners)
        if first_part_counter == 10 and second_part_counter == 10 and first_part_symbol == second_part_symbol:
            print(f'ticket "{ticket}" - {first_part_counter}{first_part_symbol} Jackpot!')
        elif first_part_symbol == second_part_symbol and 6 <= first_part_counter and second_part_counter >= 6:
            print(f'ticket "{ticket}" - {min(first_part_counter, second_part_counter)}{first_part_symbol}')
        else:
            print(f'ticket "{ticket}" - no match')
