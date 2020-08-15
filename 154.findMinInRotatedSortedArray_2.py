
class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(set(nums)) == 1:
                return nums[0]

        while nums[0] == nums[-1]:
            nums.pop(-1)

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
