from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for det in details:
            if int(det[11:13]) > 60:
                cnt += 1
        return cnt
