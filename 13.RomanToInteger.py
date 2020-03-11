
class Solution:
    def romanToInt(self, s):

        """
        :type x: str
        :rtype: int
        """

        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")

        sums = 0
        for char in s:
            sums += values[char]

        return sums

# 自我检查

def romanToInt(s):

        """
        :type x: str
        :rtype: int
        """

        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")

        print(s)
        sums = 0
        for char in s:
            sums += values[char]

        return sums

romanToInt("IV")
