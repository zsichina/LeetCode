class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num
        nums = list(str(abs(num)))
        if num > 0:
            nums.sort()
            for i in range(len(nums)):
                if nums[i] != "0":
                    nums[0], nums[i] = nums[i], nums[0]
                    break
            return int("".join(nums))
        else:
            nums.sort(reverse=True)
            return -1 * int("".join(nums))


print(__name__)
if __name__ == "__main__":
    sol = Solution()

    num = 310
    print(sol.smallestNumber(num))

    num = -7605
    print(sol.smallestNumber(num))

    num = 1000000000000000
    print(sol.smallestNumber(num))
