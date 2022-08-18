from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = (len(arr) + 1)//2
        counts = sorted(Counter(arr).values(), reverse=True)
        sm = 0
        for idx, val in enumerate(counts):
            sm += val
            if sm >= half:
                return idx + 1


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = (len(arr) + 1)//2
        counts = Counter(arr).most_common()
        sm = 0
        cnt = 0
        for _, val in counts:
            sm += val
            cnt += 1
            if sm >= half:
                break
        return cnt
