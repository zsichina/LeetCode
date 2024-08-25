from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        all_combs = defaultdict(list)
        for word in wordList:
            for i in range(n):
                all_combs[word[:i] + "*" + word[i + 1 :]].append(word)

        visited = set()
        level = 1
        q = deque([(beginWord, level)])
        while q:
            currWord, level = q.popleft()
            if currWord == endWord:
                return level
            visited.add(currWord)
            for i in range(n):
                for cand in all_combs[currWord[:i] + "*" + currWord[i + 1 :]]:
                    if cand not in visited:
                        q.append((cand, level + 1))

        return 0
