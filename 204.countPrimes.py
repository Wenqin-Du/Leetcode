class Solution:
    def countPrimes(self, n: int) -> int:

        # Method 1
        # if n <= 1:
        #     return 0
        # res = [None] * n
        # res[0], res[1] = False, False
        #
        # for i in range(n):
        #     if res[i] == None:
        #         res[i] = True
        #
        #         for j in range(2 * i, n, i):
        #             res[j] = False
        #
        # return(sum(res))

        # Method 2 a little better
        if n <= 1:
            return 0
        res = [True] * n
        res[0], res[1] = False, False

        for i in range(n // 2 + 1):
            if res[i] == True:
                res[i] = True

                for j in range(2 * i, n, i):
                    res[j] = False

        return(sum(res))
