from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        res = []

        for word in words:
            word_dict = {}
            pattern_dict = {}
            matches = True
            for i in range(len(pattern)):
                if word[i] not in word_dict:
                    word_dict[word[i]] = pattern[i]
                if pattern[i] not in pattern_dict:
                    pattern_dict[pattern[i]] = word[i]

                if word_dict[word[i]] != pattern[i] or pattern_dict[pattern[i]] != word[i]:
                    matches = False
                    break
            if matches:
                res.append(word)

        return res
