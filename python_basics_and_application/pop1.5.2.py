class Buffer:

    def __init__(self, s=[]):
        self.s = s

    def add(self, *a):
        self.a = a
        self.s += self.a
        sum = 0
        if len(self.s) >= 5:
            for o in range(len(self.s) // 5):
                for j in range(5):
                    sum += int(self.s.pop(0))
                print(sum)
                sum = 0

    def get_current_part(self):
        return self.s
