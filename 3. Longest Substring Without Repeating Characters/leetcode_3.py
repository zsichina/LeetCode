class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = defaultdict(int)
        maxCnt = 0
        start = 0
        for i in range(len(s)):
            start = charDict[s[i]] if charDict[s[i]] > start else start
            charDict[s[i]] = i + 1
            maxCnt = max(maxCnt, charDict[s[i]] - start)
        return maxCnt
