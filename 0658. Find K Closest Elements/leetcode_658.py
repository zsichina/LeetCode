from typing import List
from bisect import bisect_left


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        mid = bisect_left(arr, x)
        if mid == n or mid > 0 and abs(arr[mid-1]-x) <= abs(arr[mid]-x):
            mid -= 1

        left = right = mid
        for _ in range(k-1):
            if left == 0:
                right += 1
            elif right == n-1 or abs(arr[left-1]-x) <= abs(arr[right+1]-x):
                left -= 1
            else:
                right += 1

        return arr[left:right+1]
