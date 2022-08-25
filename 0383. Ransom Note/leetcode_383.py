from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        counter = Counter(magazine)
        for c in ransomNote:
            if counter[c] == 0:
                return False
            else:
                counter[c] -= 1

        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        counterR = Counter(ransomNote)
        counterM = Counter(magazine)
        for key, val in counterR.items():
            if val > counterM[key]:
                return False
            
        return True
