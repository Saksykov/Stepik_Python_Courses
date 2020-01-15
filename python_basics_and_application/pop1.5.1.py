class MoneyBox:

    def __init__(self, capacity = 0, coin = 0):
        self.capacity = capacity
        self.coin = coin

    def can_add(self, v):
        self.v = v
        if self.coin + self.v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        self.v = v
        if self.can_add(self.v):
            self.coin += self.v
