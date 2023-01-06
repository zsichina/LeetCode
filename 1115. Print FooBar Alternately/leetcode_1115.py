from threading import Lock
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_done = Lock()
        self.bar_done = Lock()
        self.foo_done.acquire()

    def foo(self, printFoo: "Callable[[], None]") -> None:

        for i in range(self.n):
            self.bar_done.acquire()
            printFoo()
            self.foo_done.release()

    def bar(self, printBar: "Callable[[], None]") -> None:

        for i in range(self.n):
            self.foo_done.acquire()
            printBar()
            self.bar_done.release()
