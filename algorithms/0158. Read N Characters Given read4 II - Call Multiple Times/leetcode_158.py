from typing import List


# Remove this line, before executing on LeetCode
# The read4 API is already defined for you.
def read4(buf4: List[str]) -> int:
    ...


class Solution:
    def __init__(self):
        self.chars_read = 0
        self.chars_used = 0
        self.buf4 = ["" for _ in range(4)]

    def read(self, buf: List[str], n: int) -> int:
        cnt = 0
        while cnt < n:
            if self.chars_used == self.chars_read:
                self.chars_read = read4(self.buf4)
                self.chars_used = 0

            if self.chars_read == 0:
                return cnt

            buf[cnt] = self.buf4[self.chars_used]
            self.chars_used += 1
            cnt += 1

        return cnt
