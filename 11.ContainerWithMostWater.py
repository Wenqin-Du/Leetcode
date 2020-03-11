
class Solution:
    def maxArea(self, height):

        """
        :type height: list
        :rtype: int
        """

        l = 0
        r = len(height) - 1
        area = 0

        for i in range(r, 0, -1):

            if height[l] < height[r]:
                area = max(area, i * height[l])
                l += 1

            else:
                area = max(area, i * height[r])
                r -= 1

        return area


# 解法2

class Solution:
    def maxArea(self, height):

            area, l, r = 0, 0, len(height) - 1

            while l < r:
                h = min(height[l], height[r])
                area, l, r = max(area,  h * (r - l)), l + (height[l] == h), r - (height[r] == h)

            return area
