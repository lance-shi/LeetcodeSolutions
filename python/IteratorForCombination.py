# Question No. 1286 
# Iteration for Combination
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.char = characters
        self.l = combinationLength
        self.arr = [i for i in range(combinationLength)]
        self.has_next = True

    def next(self) -> str:
        if not self.has_next:
            return False
        result = ""
        for i in range(self.l):
            result += self.char[self.arr[i]]
        self.move()
        return result

    def move(self):
        if self.arr[0] + self.l >= len(self.char):
            self.has_next = False
            return
        for i in range(self.l - 1, -1, -1):
            if self.arr[i] - i + self.l < len(self.char):
                self.arr[i] += 1
                mark = self.arr[i] + 1
                for j in range(i + 1, self.l):
                    self.arr[j] = mark
                    mark += 1
                return

    def hasNext(self) -> bool:
        return self.has_next