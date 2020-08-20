
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        if t < 0:
            return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in range(n):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] // w]
        return False

        # exceed time limit
        dic = {}
        for i, v in enumerate(nums):

            temp = []
            for key in dic:
                if abs(v-key) <= t and i - dic[key] <= k:
                    return True
                if i - dic[key] > k:
                    temp.append(key)
            dic = {key: dic[key] for key in dic if key not in temp}

            # dic = {key: dic[key] for key in dic if i - dic[key] <= k}
            dic[v] = i

        return False
