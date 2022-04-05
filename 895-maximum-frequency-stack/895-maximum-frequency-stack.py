class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        x = self.freq[val] + 1
        self.freq[val] = x
        self.group[x].append(val)
        if x >= self.max_freq:
            self.max_freq = x
        

    def pop(self) -> int:
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()