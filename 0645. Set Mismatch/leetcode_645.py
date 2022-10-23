from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
      n = len(nums)
      st = {x+1 for x in range(n)}

      duplicated = 0
      for i in range(len(nums)):
        if nums[i] in st:
          st.remove(nums[i])
        else:
          duplicated = nums[i]

      return [duplicated, st.pop()]
