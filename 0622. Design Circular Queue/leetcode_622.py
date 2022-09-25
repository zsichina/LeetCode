class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.circularQueue = [-1 for _ in range(k)]
        self.start = 0
        self.end = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.circularQueue[self.end] = value
        self.end = (self.end+1)%self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.circularQueue[self.start] = -1
        self.start = (self.start+1)%self.size
        return True

    def Front(self) -> int:
        return self.circularQueue[self.start]

    def Rear(self) -> int:
        return self.circularQueue[self.end-1]

    def isEmpty(self) -> bool:
        if self.circularQueue[self.start] == -1:
            return True
        return False

    def isFull(self) -> bool:
        if self.circularQueue[self.end] == -1 or self.start != self.end:
            return False
        return True
