from collections import defaultdict


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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fast, slow, cnt, max_length = 0, 0, 0, 0
        seen = set()
        while fast < len(s):

            while s[fast] in seen:
                seen.remove(s[slow])
                cnt -= 1
                slow += 1

            cnt += 1
            max_length = max(max_length, cnt)
            seen.add(s[fast])
            fast += 1

        return max_length
