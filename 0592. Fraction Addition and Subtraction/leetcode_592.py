class Solution:
    def _gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def fractionAddition(self, expression: str) -> str:
        final_numer, final_denom, sign, scanning_numer = 0, 1, 1, 1
        numer, denom = ("0", "1") if expression[0] == "-" else ("", "")
        signs = {"-": -1, "+": 1}
        for char in expression:
            if char in signs:
                final_numer = final_numer * int(denom) + sign * (
                    int(numer) * final_denom
                )
                final_denom *= int(denom)
                sign = signs[char]
                scanning_numer = 1
                numer = denom = ""
            elif char == "/":
                scanning_numer = 0
            elif scanning_numer:
                numer += char
            else:
                denom += char

        final_numer = final_numer * int(denom) + sign * int(numer) * final_denom
        final_denom *= int(denom)

        gcd = self._gcd(final_numer, final_denom)
        final_numer //= gcd
        final_denom //= gcd

        return f"{final_numer}/{final_denom}"


# The following is a test of the solution
def test_solution():
    solution = Solution()
    assert solution.fractionAddition("-1/2+1/2") == "0/1"
    assert solution.fractionAddition("-1/2+1/2+1/3") == "1/3"
    assert solution.fractionAddition("1/3-1/2") == "-1/6"
    assert solution.fractionAddition("5/3+1/3") == "2/1"
    assert solution.fractionAddition("5/3+1/3+1/3") == "7/3"
    assert solution.fractionAddition("5/3+1/3+1/3+1/3") == "8/3"
    assert solution.fractionAddition("5/3+1/3+1/3+1/3+1/3") == "3/1"
    assert solution.fractionAddition("5/3+1/3+1/3+1/3+1/3+1/3") == "10/3"
    assert solution.fractionAddition("5/3+1/3+1/3+1/3+1/3+1/3+1/3") == "11/3"
    assert solution.fractionAddition("5/3+1/3+1/3+1/3+1/3+1/3+1/3+1/3") == "4/1"
    assert solution.fractionAddition("5/3+1/3+1/3-1/3+1/3-1/7+1/3+1/3") == "20/7"


# run terst for the solution
test_solution()
