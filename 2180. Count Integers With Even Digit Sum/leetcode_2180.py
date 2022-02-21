class Solution:
    def countEven(self, num: int) -> int:
        if sum(int(x) for x in str(num))%2==0:
            return num//2
        return num//2 - (1-num%2)
