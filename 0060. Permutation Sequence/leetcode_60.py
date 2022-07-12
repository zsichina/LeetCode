from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k-=1
        digits = [idx for idx in range(1, n+1)]
        
        res = []
        for idx in range(n-1, -1, -1):
            q, k = divmod(k, factorial(idx))
            res.append(digits.pop(q))
        
        return "".join(map(str, res))
