class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equals = []
        greater = []
        for num in nums:
            if num<pivot:
                less.append(num)
            elif num==pivot:
                equals.append(num)
            else:
                greater.append(num)
        return less+equals+greater