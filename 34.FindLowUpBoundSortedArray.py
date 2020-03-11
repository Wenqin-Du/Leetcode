
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lowBound(nums00, target00):
            l, r = 0, len(nums00) - 1
            while l <= r:
                m = (l + r) // 2
                if nums00[m] >= target00:
                    r = m - 1
                else:
                    l = m + 1
            return l

        def upBound(nums00, target00):
            l, r = 0, len(nums00) - 1
            while l <= r:
                m = (l + r) // 2
                if nums00[m] <= target00:
                    l = m + 1
                else:
                    r = m - 1
            return r

        left, right = lowBound(nums, target), upBound(nums, target)

        if left <= right:
            return [left, right]
        else:
            return [-1, -1]





