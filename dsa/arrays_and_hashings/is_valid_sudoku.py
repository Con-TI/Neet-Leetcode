class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_counts = [defaultdict(int) for i in range(9)]
        col_counts = [defaultdict(int) for i in range(9)]
        box_counts = {(i//3,i%3):defaultdict(int) for i in range(9)}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                row_counts[i][val] += 1
                if row_counts[i][val] > 1:
                    return False
                col_counts[j][val] += 1
                if col_counts[j][val] > 1:
                    return False
                box_coord = (i//3,j//3)
                box_counts[box_coord][val] += 1
                if box_counts[box_coord][val] > 1:
                    return False
        return True


