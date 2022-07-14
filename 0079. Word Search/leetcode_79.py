from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_len = len(word)
        letters = Counter(word)

        for i in range(m):
            for j in range(n):
                if board[i][j] in letters:
                    letters[board[i][j]] -= 1
                    if letters[board[i][j]] == 0:
                        del letters[board[i][j]]
            if not letters:
                break
        if letters:
            return False
        
        def dfs(row, col, idx):
            if board[row][col] != word[idx]:
                return False
            if idx == word_len - 1:
                return True
            
            temp = board[row][col]
            board[row][col] = -1
            
            for r, c in ((row+1, col), (row, col+1), (row-1, col), (row, col-1)):
                if 0 <= r < m and 0 <= c < n:
                    if dfs(r, c, idx+1):
                        return True

            board[row][col] = temp
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


