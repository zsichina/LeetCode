class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        sums = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                if j == i + 1:
                    sm = nums[i]
                else:
                    sm = sums[-1] + nums[j - 1]
                sums.append(sm)
        sums.sort()
        print(sums)
        return sum(sums[left - 1 : right]) % (10**9 + 7)
