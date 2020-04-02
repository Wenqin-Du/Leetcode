
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[0: k], nums[k:] = nums[len(nums)-k:], nums[0: len(nums)-k]

        # Way 2
        # nums[:] = nums[-k:] + nums[:-k]
