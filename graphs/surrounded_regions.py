class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        grid =[[False] * COLS for _ in range(ROWS)]
        visited = set()
        
        def dfs(coords):
            i,j = coords
            if 0<=i<ROWS and 0<=j<COLS and coords not in visited and board[i][j] == "O":
                grid[i][j] = True
                visited.add((i,j))
                dfs((i+1,j))
                dfs((i-1,j))
                dfs((i,j+1))
                dfs((i,j-1))


        looped = set()
        for i in range(ROWS):
            if board[i][0] == "O": looped.add((i,0))
            if board[i][COLS-1] == "O" : looped.add((i,COLS-1))
        for j in range(COLS):
            if board[0][j] == "O" : looped.add((0,j))
            if board[ROWS-1][j] == "O" : looped.add((ROWS-1,j))

        for coords in looped:
            dfs(coords)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

