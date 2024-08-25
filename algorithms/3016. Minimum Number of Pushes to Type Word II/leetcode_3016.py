from collections import Counter


class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        counter = Counter(word)
        counter = sorted(counter.items(), key=lambda x: -x[1])
        buttons, cost, total = 8, 1, 0
        for _, v in counter:
            total += v * cost
            buttons -= 1
            if buttons == 0:
                cost += 1
                buttons = 8
        return total
