class Solution:
    def solveNQueens(self, n: int):
        res = []
        board = [["."] * n for _ in range(n)]

        cols = [0] * n
        diag1 = [0] * (2 * n)
        diag2 = [0] * (2 * n)

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                d1 = row + col
                d2 = row - col + (n - 1)
                if cols[col] or diag1[d1] or diag2[d2]:
                    continue

                board[row][col] = "Q"
                cols[col] = diag1[d1] = diag2[d2] = 1

                backtrack(row + 1)

                board[row][col] = "."
                cols[col] = diag1[d1] = diag2[d2] = 0

        backtrack(0)
        return res