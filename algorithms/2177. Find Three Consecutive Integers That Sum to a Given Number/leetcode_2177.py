from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        d, m = divmod(num, 3)
        if m:
            return []
        return [d - 1, d, d + 1]
