from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p1, p2, n, m = 0, 0, len(nums1), len(nums2)
        res = []
        
        while p1 < n and p2 < m:
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        return res

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            res = []
            counter1 = Counter(nums1)
            
            for num in nums2:
                if num in counter1:
                    res.append(num)
                    counter1[num] -= 1
                    if counter1[num] == 0:
                        del counter1[num]
                    if not counter1:
                        break

            return res

