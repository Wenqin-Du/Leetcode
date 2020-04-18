
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # basic
        # for n in range(len(nums) + 1):
        #     if n not in nums:
        #         return n

        # Smart move
        return sum(range(len(nums)+1)) - sum(nums)

