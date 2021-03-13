class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []
        self.index = 0

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __add__(self, other):
        temp_owner = self.owner + "&" + other.owner
        temp_amount = self.amount + other.amount
        temp_transaction = self._transactions + other._transactions
        temp = Account(temp_owner, temp_amount)
        temp._transactions = temp_transaction
        return temp

    def __getitem__(self, index):
        return self._transactions[index]

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance >= other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __len__(self):
        return len(self._transactions)

    @staticmethod
    def amount_is_not_valid(amount):
        return type(amount) != int

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def add_transaction(self, amount):
        if self.amount_is_not_valid(amount):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    def validate_transaction(self, amount_to_add):
        if self.amount_is_not_valid(amount_to_add):
            raise ValueError("please use int for amount")
        if self.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            self._transactions.append(amount_to_add)
            return f"New balance: {self.balance}"


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)

