# Solution 1 "each input would have exactly one solution" or solution will fail

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {v:i for i,v in enumerate(nums)}
        for i,v in enumerate(nums): # cannot use "for v,i in dic.items():"
                                    # dict's key cannot duplicate! See remark
                checkVal = target - v
                if checkVal in dic and dic[checkVal] != i:
                    return [i, dic[checkVal]]

# Solution 2 "each input would have exactly one solution" or solution will fail

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, v in enumerate(nums):
            if (target-v) in dic:
                return [dic[target-v],i]
            dic[v] = i


# Remark

nums = [3,3,3,3]
dic = {v:i for i,v in enumerate(nums) }
    for i,v in enumerate(nums):
    # for v,i in dic.items(): Will print out null
        checkVal = 6 - v
        if checkVal in dic and dic[checkVal] != i:
            print([i, dic[checkVal]])
# [0, 3]
# [1, 3]
# [2, 3]

for k, v in dic.items():
    print(k, v)
# 3 3

for i,v in enumerate(nums):
    print(i, v)
# 0 3
# 1 3
# 2 3
# 3 3
