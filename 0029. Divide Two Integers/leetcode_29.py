class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        cnt = 0
        coeff = 1
        divisorWithCoeff = divisor
        coeffs = []
        divisors = []

        while dividend >= divisorWithCoeff:
            coeffs.append(coeff)
            divisors.append(divisorWithCoeff)
            coeff += coeff
            divisorWithCoeff += divisorWithCoeff

        for i in range(len(divisors) - 1, -1, -1):
            while dividend >= divisors[i]:
                dividend -= divisors[i]
                if sign == 1:
                    cnt += coeffs[i]
                else:
                    cnt -= coeffs[i]

        if cnt > 2147483647:
            cnt = 2147483647
        elif cnt < -2147483648:
            cnt = -2147483648

        return cnt
