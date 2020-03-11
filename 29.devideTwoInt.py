
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        a = abs(dividend)
        b = abs(divisor)

        if a < b or a == 0:
            return 0

        sums, count, res = 0, 0, 0

        while a >= b:
            sums = b
            count = 1
            while a >= sums + sums:
                sums += sums
                count += count
            a -= sums
            res += count

        if res >= 2**31 and (2 * (dividend > 0)-1) * (2 * (divisor >= 0) - 1) == 1:
            return 2**31 - 1

        return res * (2 * (dividend > 0)-1) * (2 * (divisor >= 0) - 1)





def divide(dividend: int, divisor: int) -> int:

        a = abs(dividend)
        b = abs(divisor)

        if a < b or a == 0:
            return 0

        sums, count, res = 0, 0, 0

        while a >= b:
            sums = b
            count = 1
            while a >= sums + sums:
                sums += sums
                count += count
            a -= sums
            res += count

        return res * (2 * (dividend > 0)-1) * (2 * (divisor >= 0) - 1)

print(divide(-2147483648, -1))
