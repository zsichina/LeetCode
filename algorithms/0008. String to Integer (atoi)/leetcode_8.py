class Solution:
    def myAtoi(self, s: str) -> int:
        d = ""
        s = s.lstrip(" ")

        if len(s) == 0:
            return 0

        sign = 1
        if s[0] == "+":
            s = s[1:]
            if len(s) == 0:
                return 0
        elif s[0] == "-":
            sign = -1
            s = s[1:]
            if len(s) == 0:
                return 0

        for i in range(len(s)):
            if not s[i].isdigit():
                break
            d += s[i]

        res = sign * int(d or 0)

        if res > 2**31 - 1:
            res = 2**31 - 1
        elif res < -(2**31):
            res = -(2**31)

        return res
