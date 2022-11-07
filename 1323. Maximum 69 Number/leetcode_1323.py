class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        start, end = 0, n-1
        for start in range(n):
            if s[start] == "6":
                s[start] = "9"
                break

        return int("".join(s))
