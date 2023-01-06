from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapNum(num):
            ans = ""
            for n in str(num):
                ans += str(mapping[int(n)])
            return int(ans)

        nums = sorted(nums, key=lambda x: mapNum(x))

        return nums
