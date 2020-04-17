
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False

        i, j = 0, len(matrix[0])-1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else: return True

        return False

        # for i in range(len(matrix)):
        #     if target in matrix[i]:
        #         return True
        # return False
