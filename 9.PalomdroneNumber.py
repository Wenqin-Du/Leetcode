
class Solution:
    def isPalindrome(self, x):

        """
        :type x: int
        :rtype: boolean
        """

        if x < 0:
            return False

        para, rev = x, 0

        while para:
            rev = 10 * rev + para % 10
            para = int(para/10)

        return rev == x


# second approach

class Solution:
    def isPalindrome(self, x):

        """
        :type x: int
        :rtype: boolean
        """

        return int(str(abs(x))[::-1]) == x
