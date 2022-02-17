class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                d, num1 = divmod(num1, num2)
            else:
                d, num2 = divmod(num2, num1)
            cnt += d
        return cnt
