from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        cnt = 0
        max_fruits = 0
        baskets = {}
        fast, slow = 0, 0
        while fast < n:
            if fruits[fast] not in baskets:
                baskets[fruits[fast]] = 1
                cnt += 1
            else:
                baskets[fruits[fast]] += 1

            while cnt > 2:
                baskets[fruits[slow]] -= 1
                if baskets[fruits[slow]] == 0:
                    del baskets[fruits[slow]]
                    cnt -= 1
                slow += 1

            max_fruits = max(max_fruits, fast - slow + 1)

            fast += 1

        return max_fruits
