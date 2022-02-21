from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter = {}
        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]].append(i)
            else:
                counter[nums[i]]= [i]

        ans = 0
        for key, val in counter.items():
            length = len(val)
            for i in range(length-1):
                for j in range(i+1, length):
                    if val[i] * val[j] % k == 0:
                        ans += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    
    nums = [3,1,2,2,2,1,3]
    k = 2
    print(sol.countPairs(nums, k)==4)

    nums = [1,2,3,4]
    k = 1
    print(sol.countPairs(nums, k)==0)

    nums = [10,2,3,4,9,6,3,10,3,6,3,9,1]
    k = 4
    print(sol.countPairs(nums, k)==8)