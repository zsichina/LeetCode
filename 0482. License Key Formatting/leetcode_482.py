class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        res = ""
        s = s.upper().replace("-", "")[::-1]
        
        for i in range(0, len(s), k):
            res += s[i:i+k] + "-"
                        
        return res[::-1].strip("-")

