class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        n = len(s)
        for i in range(n-1, -1, -1):
            if s[i] == " ":
                return n-1-i
        return n
        
    # def lengthOfLastWord(self, s: str) -> int:
    #     return len(s.split()[-1])

