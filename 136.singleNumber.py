
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
        return nums[0]  # No extra memory


        # Solution 2
        # res = 0
        # for num in nums:
        #     res ^= num
        # return res


        # Solution 3
        # counts = dict()

        # for i in nums:
        #     if i in counts:
        #         counts[i] += 1
        #     else:
        #         counts[i] = 1

        # for key in counts:
        #     if counts[key] == 1:
        #         return key


