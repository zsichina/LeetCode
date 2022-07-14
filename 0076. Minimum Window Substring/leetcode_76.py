from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len1 = len(s)
        len2 = len(t)
        if len2>len1:
            return ""
        dictT = Counter(t)
        cnt = len2
        l=r=0
        lBound, rBound = 0, len1
        found = False
        while r<len1:
            if s[r] in dictT:
                if dictT[s[r]]>0:
                    cnt-=1
                dictT[s[r]]-=1
            while cnt==0:
                found = True
                if rBound-lBound>r-l:
                    rBound, lBound = r, l
                if s[l] in dictT:
                    dictT[s[l]]+=1
                if dictT[s[l]]>0:
                    cnt+=1
                l+=1
            r+=1

        return s[lBound:rBound+1] if found else ""
