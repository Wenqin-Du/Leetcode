
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # if len(nums) == 0:
        #     return 0

        if max(nums) <= 0:
            return max(nums)

        sums = 0
        posi = 0
        for num in nums:

            if num > 0 >= sums and num > posi:
                posi = num
                sums = num
            else:
                sums += num

        return max(posi, sums)





def maxSubArray(nums):

        # if len(nums) == 0:
        #     return 0

        if max(nums) <= 0:
            return max(nums)

        sums = 0
        posi = 0  # track 最大的正项
        track = 0  # track 最大的和数
        for num in nums:

            if num > 0 >= sums:
                posi = max(num, posi)
                sums = num
            else:
                sums += num

            track = max(sums, posi, track)

        return track


maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

maxSubArray([8,-19,5,-4,20])
