from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        counter = Counter(words)
        add_two = False
        for word, cnt in counter.items():
          reverse = word[::-1]
          if word == reverse:
            if cnt%2 == 1:
              add_two = True
            res += (cnt//2)*4
            counter[word] -= (cnt//2)*2
          elif reverse in counter:
            match_cnt = min(counter[reverse], cnt)
            res += match_cnt*4
            counter[reverse] -= match_cnt
            counter[word] -= match_cnt

        res += 2 if add_two else 0
        return res
