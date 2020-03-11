
class Solution:

    def longestPalindrome(self, s):

        """ 多行注释方法
        :type s: str
        :rtype: str
        """

        ans = ""

        for i in range(len(s)):
            ans = max(self.palindomCheck(i, i, s), self.palindomCheck(i, i+1, s), ans, key=len)

        return ans

    def palindomCheck(self, l, r, s):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]  # NOT include r^th element!!!


# check

def palindomCheck(l, r, s):

    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
        print(l,r)
    return s[l+1:r]

print(palindom(2, 2, "qabacd"))
