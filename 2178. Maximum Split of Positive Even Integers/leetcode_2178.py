from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        else:
            ans = []
            i = 0
            while finalSum:
                if 2 * i + 6 > finalSum:
                    ans.append(finalSum)
                    break
                else:
                    i += 2
                    ans.append(i)
                    finalSum -= i
        return ans
