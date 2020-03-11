
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        clThreeS = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l, r = i+1, len(nums)-1
            while l < r:
                threeS = nums[i] + nums[l] + nums[r]
                if abs(threeS - target) < abs(clThreeS - target):
                    clThreeS = threeS
                if threeS < target:
                    l += 1
                elif threeS > target:
                    r -= 1
                else:
                    return target

        return clThreeS
