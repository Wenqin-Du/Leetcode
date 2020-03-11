
class Solution:

    def reverse(self, x):

        """
        :type x: int
        :rtype: int
        """

        s = x > 0 - x < 0
        v = int(str(s * x)[::-1])  # 等价于 int('s * x'[::-1])
        return s * v * (v < 2 ** 31)


