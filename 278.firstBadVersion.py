
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Method 1
        if isBadVersion(1):
            return 1

        l, r = 0, n
        while l < r:
            mid = (l+r) // 2
            if not isBadVersion(mid):
                l = mid
            else:
                r = mid
            if (not isBadVersion(l)) and isBadVersion(l+1):
                return l + 1

        # Method 2
        l,r = 0, n
        while l < r:
            mid = (l+r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
        return l




