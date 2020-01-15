# Итераторы и генераторы
class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(pos, neg):
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for i in self.iterable:
            self.pos = 0
            self.neg = 0
            for j in self.funcs:
                if j(i):
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(self.pos, self.neg):
                yield i