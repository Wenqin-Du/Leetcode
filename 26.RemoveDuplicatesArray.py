
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = track = 1
        while track < len(nums):
            if nums[track - 1] != nums[track]:
                nums[count] = nums[track]
                count += 1
            track += 1
        return count
