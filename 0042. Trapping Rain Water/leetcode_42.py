from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        st = []
        curr = 0
        while curr < len(height):
            while st and height[curr] > height[st[-1]]:
                top = st.pop()
                if not st:
                    break
                distance = curr - st[-1] - 1
                bounded_height = min(height[curr], height[st[-1]]) - height[top]
                res += distance * bounded_height
            st.append(curr)
            curr += 1

        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        res, n = 0, len(height)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        left[0], right[n - 1] = height[0], height[n - 1]

        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
            right[n - 1 - i] = max(right[n - i], height[n - 1 - i])

        for i in range(n):
            res += min(left[i], right[i]) - height[i]

        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        res, start, end, left_max, right_max = 0, 0, len(height) - 1, 0, 0
        while start < end:
            if height[start] < height[end]:
                if height[start] >= left_max:
                    left_max = height[start]
                else:
                    res += left_max - height[start]
                start += 1
            else:
                if height[end] >= right_max:
                    right_max = height[end]
                else:
                    res += right_max - height[end]
                end -= 1

        return res
