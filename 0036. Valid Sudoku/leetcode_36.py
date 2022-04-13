from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            dic  = {}
            dic1 = {}
            dic2 = {}
            for j in range(9):
                if board[i][j] != "." and board[i][j] in dic:
                    return False
                dic[board[i][j]] = 1
                if board[j][i] != "." and board[j][i] in dic1:
                    return False
                dic1[board[j][i]] = 1
                if board[i//3*3 + j//3][i%3*3 + j%3] != "." and board[i//3*3 + j//3][i%3*3 + j%3] in dic2:
                    return False
                dic2[board[i//3*3 + j//3][i%3*3 + j%3]] = 1

        return True

if __name__ == '__main__':
    matrix = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    sol = Solution()
    print(sol.isValidSudoku(matrix))