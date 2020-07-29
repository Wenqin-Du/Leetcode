
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(range(1, n+1), k, 0, [], res)
        return res

    def dfs(self, nums, k, index, path, res):
        if k == 0:
            res.append(path)
            return  # backtracking

        if self.valid(nums, k, index):  # pruning
            for i in range(index, len(nums)):
                self.dfs(nums, k-1, i+1, path + [nums[i]], res)

    def valid(self, n, k, i):  # pruning
        if len(n) - i < k:
            return False
        return True
