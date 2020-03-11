
class Solution:
    def spiralOrder(self, matrix):
        print(matrix)
        print(000)

        return matrix and matrix.pop(0) + self.spiralOrder([*zip(*matrix)][::-1])






def spiralOrder(matrix):

    return 2 and matrix and 0 and [] and 5


a = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Solution().spiralOrder(a)

spiralOrder(a)
