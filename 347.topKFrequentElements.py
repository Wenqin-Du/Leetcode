
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        res = []
        for key in counts:
            res.append([key, counts[key]])
        res = sorted(res, key = lambda x: x[1], reverse = True)

        return [res[i][0] for i in range(k)]

