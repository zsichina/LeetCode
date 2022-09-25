from typing import Callable
from threading import Lock, Barrier


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_done = Lock()
        self.odd_even = 0
        self.even_barrier = Barrier(2)
        self.odd_barrier = Barrier(2)

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.zero_done.acquire()
            printNumber(0)
            if self.odd_even == 0:
                self.odd_barrier.wait()
            else:
                self.even_barrier.wait()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n//2):
            self.even_barrier.wait()
            printNumber((i+1)*2)
            self.odd_even = 0
            self.zero_done.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range((self.n+1)//2):
            self.odd_barrier.wait()
            printNumber(i*2+1)
            self.odd_even = 1
            self.zero_done.release()
