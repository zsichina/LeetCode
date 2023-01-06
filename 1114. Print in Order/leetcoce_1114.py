from threading import Lock
from typing import Callable


class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: "Callable[[], None]") -> None:
        printFirst()
        self.firstJobDone.release()

    def second(self, printSecond: "Callable[[], None]") -> None:
        with self.firstJobDone:
            printSecond()
            self.secondJobDone.release()

    def third(self, printThird: "Callable[[], None]") -> None:
        with self.secondJobDone:
            printThird()
