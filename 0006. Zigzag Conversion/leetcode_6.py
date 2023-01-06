class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        arr = ["" for x in range(min(numRows, len(s)))]
        goingUp = True
        currRow = 0
        for val in s:
            arr[currRow] += val
            if currRow == 0 or currRow == numRows - 1:
                goingUp = not goingUp
            currRow += -1 if goingUp else 1
        return "".join(arr)
