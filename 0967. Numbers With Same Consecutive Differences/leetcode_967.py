from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = set()
        def generate(num, left):

            if left == 0:
                res.add(num)
                return

            r = num%10
            if r - k >= 0:
                generate(num*10+r-k, left-1)
            if r + k < 10:
                generate(num*10+(r+k)%10, left-1)

        for i in range(1, 10):
            generate(i, n-1)

        return res
