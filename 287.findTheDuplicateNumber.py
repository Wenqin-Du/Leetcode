
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Direct way
        while nums:
            temp = nums[0]
            nums.remove(temp)
            if temp in nums:
                return temp

        # Sort way
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                return nums[i]


        # Binary search (value)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if sum(i <= mid for i in nums) > mid:
                right = mid
            else:
                left = mid + 1
        return left
        
