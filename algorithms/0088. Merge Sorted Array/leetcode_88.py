from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        for pointer3 in reversed(range(m + n)):
            if pointer2 < 0 or pointer1 >= 0 and nums1[pointer1] >= nums2[pointer2]:
                nums1[pointer3] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[pointer3] = nums2[pointer2]
                pointer2 -= 1
