class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        d = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for bracket in s:
            if bracket in d:
                stack.append(bracket)
            elif not stack or d[stack.pop()] != bracket:
                return False

        return not stack
