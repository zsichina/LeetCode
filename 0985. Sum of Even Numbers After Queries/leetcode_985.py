from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_of_even = 0
        for val in nums:
            if val%2 == 0:
                sum_of_even += val

        answer = []
        for val, idx in queries:
            if nums[idx]%2 == 0:
                if val%2 == 0:
                    sum_of_even += val
                else:
                    sum_of_even -= nums[idx]
            else:
                if val%2 == 1:
                    sum_of_even += val + nums[idx]
            nums[idx] += val
            answer.append(sum_of_even)

        return answer
