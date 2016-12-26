import math


class SegmentTree:
    def __init__(self, string):
        self.string = string
        self.length = len(string)
        self.segment_tree = []
        self.__build(string)

    def __build(self, string):
        for i in range(2 * self.length):
            if i < self.length:
                self.segment_tree.append(Brackets(0, 0, 0))
            else:
                if string[i - len(string)] == '(':
                    self.segment_tree.append(Brackets(1, 0, 0))
                else:
                    self.segment_tree.append(Brackets(0, 1, 0))
        for i in range(self.length - 1, 0, -1):
            self.segment_tree[i] = self.segment_tree[2 * i] + self.segment_tree[2 * i + 1]

    def __query(self, current, left, right, l, r):
        if l == left and r == right:
            return self.segment_tree[current]
        elif r <= (left + right) // 2:
            return self.__query(current * 2, left, (left + right) // 2, l, r)
        elif l > (left + right) // 2:
            return self.__query(current * 2 + 1, (left + right) // 2 + 1, right, l, r)
        else:
            return self.__query(current * 2, left, (left + right) // 2, l, (left + right) // 2) + \
                   self.__query(current * 2 + 1, (left + right) // 2 + 1, right, (left + right) // 2 + 1, r)

    def query(self, l, r):
        q = self.__query(1, 0, len(self.string) - 1, l - 1, r - 1)
        return q.bal

    def print_tree(self):
        count = 0
        for e in self.segment_tree:
            print(count, 'узел', e)
            count += 1


class Brackets:
    def __init__(self, open, close, bal):
        self.open = open
        self.close = close
        self.bal = bal

    def __str__(self):
        return 'макс сбалансир: ' + str(self.bal)

    def __add__(self, other):
        bal = self.bal + other.bal
        new_bal = min(self.open, other.close)
        new_open = self.open + other.open - new_bal
        new_close = self.close + other.close - new_bal
        return Brackets(new_open, new_close, bal + new_bal)

brackets = ')(()())'
length = 2 ** math.ceil(math.log2(len(brackets)))
brackets += (length - len(brackets)) * '('
print(brackets)
segment_tree = SegmentTree(brackets)
segment_tree.print_tree()

print(segment_tree.query(1, 5))
print(segment_tree.query(2, 6))
print(segment_tree.query(2, 7))
