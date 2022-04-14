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
