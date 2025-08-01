class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Backtracking
        res = []
        board = [["."]*n for i in range(n)]
        # r keeps track of how many queens have been placed so far and which row we 
        # are trying to fill
        # in a run/track
        def backtrack(r):
            if r == n:
                # Convert board matrix into row by row string
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # If you can place a queen at (r,c) safely
                # Do so and try placing the next queen
                if self.isSafe(r,c,board):
                    board[r][c] = "Q"
                    backtrack(r+1)
                    board[r][c] = "."

        backtrack(0)
        return res

    def isSafe(self, r: int, c: int, board):
        row = r - 1
        # Check if up-down is hit, starting from the current row to the 0th
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
        
        # Check if diagonals are hit, starting from the current row to the 0th
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1

        return True