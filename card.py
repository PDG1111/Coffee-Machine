class Card:
    def __init__(self, id, user_type, name, balance):
        self.id = id
        self.user_type = user_type
        self.name = name
        self.balance = float(balance)

    def pay(self, amount):
        self.balance -= float(amount)
