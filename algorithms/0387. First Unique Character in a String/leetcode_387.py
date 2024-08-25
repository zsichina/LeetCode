from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for idx, val in enumerate(s):
            if counter[val] == 1:
                return idx

        return -1
