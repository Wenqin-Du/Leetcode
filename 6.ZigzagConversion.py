
class Solution:

    def convert(self, s, numRows):

        if len(s) <= numRows or numRows == 1:
            return s

        l = [''] * numRows
        index = 0; step = 0
        #  index, step = 0, 1

        for cha in s:

            l[index] += cha

            if index == 0:
                step = 1

            elif index == numRows - 1:
                step = -1

            index += step

        return ''.join(l)
