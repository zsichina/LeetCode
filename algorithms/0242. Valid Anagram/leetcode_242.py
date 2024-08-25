from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        for key, val in s_counter.items():
            if key not in t_counter or t_counter[key] != val:
                return False

        return True
