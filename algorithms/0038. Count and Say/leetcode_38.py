class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        toSay = self.countAndSay(n - 1)
        currChar = toSay[0]
        cnt = 0
        res = ""
        for c in toSay:
            if c == currChar:
                cnt += 1
            else:
                res += str(cnt) + currChar
                cnt = 1
                currChar = c
        res += str(cnt) + currChar

        return res
