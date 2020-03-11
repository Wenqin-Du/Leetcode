
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i, j, k = 0, 0, len(nums)

        while j < k:
            if nums[j] < 1:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j += 1
            elif nums[j] > 1:
                k -= 1
                temp = nums[j]
                nums[j] = nums[k]
                nums[k] = temp
            else:
                j += 1

        return
