
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos +=1

        for i in range(pos, len(nums)):
            nums[i] = 0


        # Wrong Order

        # l, r = 0, len(nums) - 1
        # while l < r:
        #     if nums[l] == 0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         r -= 1
        #     l += 1
