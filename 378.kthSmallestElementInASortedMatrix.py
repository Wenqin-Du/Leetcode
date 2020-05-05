
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # dummy way
        # res = []
        # for r in matrix:
        #     res += r
        # return sorted(res)[k-1]

        def equalOrSmaller(matrix, x):
            i, j, count = len(matrix) - 1, 0, 0
            while i >= 0 and j < len(matrix[0]):
                if matrix[i][j] <= x:
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            return count

        s, l = matrix[0][0], matrix[len(matrix) - 1][len(matrix[0]) - 1]
        while s < l:
            m = (s + l) // 2
            if equalOrSmaller(matrix, m) < k:
                s = m + 1
            else:
                l = m
        return s
