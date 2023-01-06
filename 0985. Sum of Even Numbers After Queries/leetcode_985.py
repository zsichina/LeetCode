from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_of_even = sum([x for x in nums if x % 2 == 0])

        answer = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                sum_of_even -= nums[idx]

            nums[idx] += val

            if nums[idx] % 2 == 0:
                sum_of_even += nums[idx]

            answer.append(sum_of_even)

        return answer
