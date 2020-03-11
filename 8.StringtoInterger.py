
class Solution(object):

    def myAtoi(self, s):

        """
        :type str: str
        :rtype: int
        """

        list_s = list(s.strip())
        if len(list_s) == 0:
            return 0

        if list_s[0] == '-':
            sign = -1
        else:
            sign = 1

        if list_s[0] == '-' or list_s[0] == '+':
            del list_s[0]

        temp, i = 0, 0
        while i < len(list_s) and list_s[i].isdigit():
            temp = temp * 10 + ord(list_s[i]) - ord('0')
            i += 1


# check

def myAtoi(s):

    list_s = list(s.strip())
    if len(list_s) == 0:
        return 0

    if list_s[0] == '-':
        sign = -1
    else:
        sign = 1

    if list_s[0] == '-' or list_s[0] == '+':
        del list_s[0]

    temp, i = 0, 0
    while i < len(list_s) and list_s[i].isdigit():
        temp = temp * 10 + ord(list_s[i]) - ord('0')
        i += 1

    return max(-2**31, min(sign*temp, 2**31-1))


print(myAtoi('-233232dwedfwd'))

print(myAtoi('        '))
