from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        def helper(i, currString):
            if len(currString) == len(digits):
                res.append(currString)
                return
            for c in digitToLetters[int(digits[i])]:
                helper(i + 1, currString + c)

        res = []
        digitToLetters = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        helper(0, "")

        return res
