
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        s, r = 0, 0

        for i in range(len(gas)):
            r += gas[i] - cost[i]
            if r < 0:
                s = i + 1
                r = 0
        return s


# slow solution
#         i = 0  # index

#         for i in range(len(gas)):
#             curr = gas[i]
#             # print('\n',i)

#             for j in range(i, i + len(gas)):
#                 curr -= cost[j - (j >= len(gas)) * len(gas)]
#                 if curr >= 0:
#                     # print(curr)
#                     if j == i + len(gas) - 1: return i
#                     curr += gas[j + 1 - ((j + 1) >= len(gas)) * len(gas)]
#                 else: break

#         return -1



