
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, word, i, j, 0): return True
        return False

    def search(self, board, word, i, j, d):

        if i > len(board) - 1 or j > len(board[0]) - 1 or i < 0 or j < 0:
            return False

        if word[d] != board[i][j]:
            return False

        if d == len(word) - 1:
            return True

        cur = board[i][j]
        board[i][j] = 0
        found = bool(self.search(board, word, i+1, j, d+1) or self.search(board, word, i-1, j, d+1) or self.search(board, word, i, j+1, d+1) or self.search(board, word, i, j-1, d+1))
        board[i][j] = cur

        return found


# 也可以不创建 self 函数

#       def search(i, j, d):

#             if i > (len(board) - 1) or (j > len(board[0]) - 1) or i < 0 or j < 0:
#                 return False

#             if word[d] != board[i][j]:
#                 return False

#             if d == len(word) - 1:
#                 return True

#             cur = board[i][j]
#             board[i][j] = 0
#             found = bool(search(i+1,j,d+1) or search(i-1,j,d+1) or search(i,j+1,d+1) or search(i,j-1,d+1))
#             board[i][j] = cur

#             return found


#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if search(i, j, 0): return True
#         return False





