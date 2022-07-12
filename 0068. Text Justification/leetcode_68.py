from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        line = ""
        cnt=0
        lineWords = []
        res = []
        for word in words:
            if cnt==0:
                cnt=len(word)
                lineWords.append(word)
            elif cnt + 1 + len(word) <= maxWidth:
                cnt += 1 + len(word)
                lineWords.append(word)
            elif len(lineWords) == 1:
                res.append(lineWords[0].ljust(maxWidth, " "))
                cnt=len(word)
                lineWords = [word]
            else:
                q,r = divmod(maxWidth - sum(len(s) for s in lineWords), len(lineWords)-1)
                for c in lineWords:
                    line += c + " "*q
                    if r>0:
                        line+=" "
                        r-=1
                res.append(line.rstrip(" "))
                line = ""
                cnt=len(word)
                lineWords = [word]

        for c in lineWords:
            line += c + " "

        res.append(line.rstrip(" ").ljust(maxWidth, " "))
        return res
