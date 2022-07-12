from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            quotient, remainder = divmod(digits[i] + 1, 10)
            digits[i] = remainder
            if not quotient:
                return digits

        return [quotient] + digits

