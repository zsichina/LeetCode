class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n


class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0


class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        return bin(n).count("1") == 1
