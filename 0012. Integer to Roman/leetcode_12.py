class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        if num // 1000 > 0:
            for i in range(num // 1000):
                roman += "M"
        num = num % 1000

        if num // 100 == 9:
            roman += "CM"
        elif num // 100 >= 5:
            roman += "D"
            for i in range(5, num // 100):
                roman += "C"
        elif num // 100 == 4:
            roman += "CD"
        else:
            for i in range(num // 100):
                roman += "C"
        num = num % 100

        if num // 10 == 9:
            roman += "XC"
        elif num // 10 >= 5:
            roman += "L"
            for i in range(5, num // 10):
                roman += "X"
        elif num // 10 == 4:
            roman += "XL"
        else:
            for i in range(num // 10):
                roman += "X"
        num = num % 10

        if num == 9:
            roman += "IX"
        elif num >= 5:
            roman += "V"
            for i in range(5, num):
                roman += "I"
        elif num == 4:
            roman += "IV"
        else:
            for i in range(num):
                roman += "I"

        return roman


# class Solution:
#   def intToRoman(self, num):
#       values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
#       numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
#       res = ""
#       for i, v in enumerate(values):
#           res += (num//v) * numerals[i]
#           num %= v
#       return res
