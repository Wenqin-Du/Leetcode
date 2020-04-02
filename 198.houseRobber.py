
class Solution:
    def rob(self, nums: List[int]) -> int:

        # Recursuon + Memorization

        # memo, rob = 0, 0
        # for num in nums:
        #     memo, rob = rob, max(memo + num, rob)
        # return rob

        # DP

        if not nums:
            return(0)

        elif len(nums) < 3:
            return(max(nums))

        dp = [0] * len(nums)
        dp[0:2] = nums[0:2]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return(dp[-1])
