
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:  # if not any(board)
            return

        n = len(board)
        m = len(board[0])

        def dfs(i, j):

            if (not 0 <= i < n) or (not 0 <= j < m) or board[i][j] != 'O':
                return

            board[i][j] = 'G'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "G":
                    board[i][j] = "O"


