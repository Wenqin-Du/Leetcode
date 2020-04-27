
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(dp[j] * (nums[i] > nums[j]) + 1 for j in range(i))
        return max(dp)


