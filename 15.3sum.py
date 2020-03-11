
class Solution:
    def threeSum(self, nums):

        """
        :type strs: List[int];
        rtype: List[List[int]]
        """

        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if nums[i] > 0:   # 和不可能为0了
                break
            if i > 0 and nums[i] == nums[i-1]:   # 小心不要漏掉 i > 0 ！！
                continue   # 避免重复

            l = i+1
            r = len(nums)-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])   # 和等于0

                    # 重要！以下语句在 else 语句中！！
                    while l < r and nums[l] == nums[l+1]:   # 避免重复
                        l += 1
                    while nums[r] == nums[r-1] and l < r:   # 避免重复
                        r -= 1

                    l += 1   # 小心不要漏掉！！
                    r -= 1   # 小心不要漏掉！！

        return res




# 自我检查及函数补充

a = [3,4,5,1,2]
a.sort()
print(a)
