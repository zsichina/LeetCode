class Solution:
    def minimumDeletions(self, s: str) -> int:
        cntb, min_del = 0, 0
        for c in s:
            if c == "a":
                min_del = min(min_del + 1, cntb)
            else:
                cntb += 1

        return min_del
