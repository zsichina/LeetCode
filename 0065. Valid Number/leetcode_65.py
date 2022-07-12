import re

class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.fullmatch("(\+|\-)?(([0-9]+\.|[0-9]+\.[0-9]+|\.[0-9]+){1}|[0-9]+){1}((e|E)(\+|\-)?[0-9]+)?", s))
