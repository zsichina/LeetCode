class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        subtract = {"I": ("V", "X"), "X": ("L", "C"), "C": ("D", "M")}

        ans = 0

        for idx, val in enumerate(s):
            if val in subtract and idx < len(s) - 1 and s[idx + 1] in subtract[val]:
                ans -= roman_to_num[val]
            else:
                ans += roman_to_num[val]

        return ans
