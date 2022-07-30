from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        max_dict = {}
        for word in words2:
            d = Counter(word)
            for key, val in d.items():
                if key not in max_dict:
                    max_dict[key] = val
                elif max_dict[key] < val:
                    max_dict[key] = val
            
        for word in words1:
            d = Counter(word)
            is_universal = True
            for key, val in max_dict.items():
                if key not in d or d[key] < val:
                    is_universal = False
                    break
            if is_universal:
                res.append(word)
        
        return res
