from collections import Counter


class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        counter = Counter(arr)
        cnt = 0
        for elem in arr:
            if counter[elem] == 1:
                cnt += 1
            if cnt == k:
                return elem
        return ""
