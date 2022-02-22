class Bitset:
    def __init__(self, size: int):
        self.bitset = [0 for x in range(size)]
        self.flipped = False
        self.size = size
        self.sm = 0

    def fix(self, idx: int):
        self.sm += (self.bitset[idx]^int(self.flipped==False))
        self.bitset[idx] = int(self.flipped==False)

    def unfix(self, idx: int):
        self.sm -= self.bitset[idx]^int(self.flipped==True)
        self.bitset[idx] = int(self.flipped==True)

    def flip(self):
        self.flipped = not self.flipped
        self.sm = self.size - self.sm

    def all(self): return self.sm == self.size
    def one(self): return self.sm > 0
    def count(self): return self.sm

    def toString(self):
        return ''.join(str(x) for x in self.bitset) if not self.flipped else ''.join(str(x^1) for x in self.bitset)
