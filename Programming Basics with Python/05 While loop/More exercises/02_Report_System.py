money_target = int(input())
money_collect = 0
transaction_counter = 0
cash = 0
card = 0
transaction_cash = 0
transaction_card = 0
while money_target > money_collect:
    transaction_input = input()
    if transaction_input == "End":
        print("Failed to collect required money for charity.")
        break
    transaction_counter += 1
    if (transaction_counter % 2 == 1 and int(transaction_input) > 100) or (
            transaction_counter % 2 == 0 and int(transaction_input) < 10):
        print("Error in transaction!")
    elif transaction_counter % 2 == 1 and int(transaction_input) <= 100:
        print("Product sold!")
        transaction_cash += 1
        cash += int(transaction_input)
        money_collect += int(transaction_input)
    elif transaction_counter % 2 == 0 and int(transaction_input) >= 10:
        print("Product sold!")
        transaction_card += 1
        card += int(transaction_input)
        money_collect += int(transaction_input)
if money_target <= money_collect:
    print(f"Average CS: {(cash / transaction_cash):.2f}\nAverage CC: {(card / transaction_card):.2f}")
