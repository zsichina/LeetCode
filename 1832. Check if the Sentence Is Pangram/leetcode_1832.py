from collections import Counter


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counter = Counter(sentence)

        for i in range(26):
          if chr(ord("a")+i) not in counter:
            return False

        return True
