
class Solution:
    def reverseBits(self, n: int) -> int:

        n = "{0:032b}".format(n)
        return int(n[::-1],2)

