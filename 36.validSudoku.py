
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        check = sum(([(i, n), (n, j), (i // 3, j // 3, n)]
                    for i, row in enumerate(board)
                    for j, n in enumerate(row)
                    if n != '.'), [])

        return len(check) == len(set(check))



