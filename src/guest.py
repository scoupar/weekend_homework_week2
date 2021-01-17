class Guest:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def pay_fee(self, room):
        self.wallet -= room.entry_fee
        room.till += room.entry_fee
