
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # Time Complexity: O(N)

        size = len(nums)
        for i in range(1, size - 1):
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                return i
        return [0, size-1][nums[0] < nums[size - 1]]

        # Time Complexity: O(log(N))

        # left, right = 0, len(nums)-1
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] < nums[mid + 1]:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return left

