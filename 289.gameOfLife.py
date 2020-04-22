
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                lives = 0
                for x in range(max(0, i-1), min(len(board), i+2)):
                    for y in range(max(0, j-1), min(len(board[0]), j+2)):
                        if x!= i or y !=j:
                            lives += board[x][y] & 1
                if lives == 3 or lives == 2 and board[i][j] & 1:
                    board[i][j] |= 0b10

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1



