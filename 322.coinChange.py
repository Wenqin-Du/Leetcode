
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort(reverse = True)
        print(coins)
        self.ans = float('inf')
        self.dfs(coins, 0, amount, 0)
        return self.ans if self.ans != float('inf') else -1


    def dfs(self, coins, s, amount, count):

        if s == len(coins) - 1:
            if amount % coins[s] == 0:
                self.ans = min(self.ans, count + amount // coins[s])

        else:
            if count + amount // coins[s] < self.ans:
                for k in range(amount // coins[s], -1, -1):
                    self.dfs(coins, s + 1, amount - k * coins[s], count + k)


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:

#         def dfs(coins, s, amount, count):
#             if s == len(coins) - 1:
#                 if amount % coins[s] == 0:
#                     self.ans = min(self.ans, count + amount // coins[s])
#                     # print(self.ans)

#             else:
#                 if count + amount // coins[s] < self.ans:
#                     for k in range(amount // coins[s], -1, -1):
#                         dfs(coins, s + 1, amount - k * coins[s], count + k)


#         coins.sort(reverse = True)
#         print(coins)
#         self.ans = float('inf')
#         dfs(coins, 0, amount, 0)
#         return self.ans if self.ans != float('inf') else -1



