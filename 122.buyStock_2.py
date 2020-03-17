
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        pro, lb = 0, float('inf')

        for p in prices:
            lb = min(lb, p)
            if p > lb:
                pro += p - lb
                lb = p

        return pro
