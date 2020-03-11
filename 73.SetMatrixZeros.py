
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_row, zero_cloum = False, False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    if i == 0:
                        zero_row = True
                    if j == 0:
                        zero_cloum = True

                    # zero_row = True if i == 0 else zero_row
                    # zero_cloum = True if j == 0 else zero_cloum

        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0]*n

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if zero_row:
            matrix[0] = [0]*n

        if zero_cloum:
            for i in range(m):
                    matrix[i][0] = 0

        return


