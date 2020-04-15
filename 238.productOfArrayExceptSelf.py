
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prod = 1
        for i in range(1,len(nums)):
            prod *= nums[i-1]
            res[i] = prod

        prod = 1
        for i in range(len(nums)-2, -1, -1):
            prod *= nums[i+1]
            res[i] *= prod

        return res


        # Time Limit Exceeded

        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     res[i] = reduce(lambda x,y: x*y, nums[:i] + nums[i+1:])
        # return res



