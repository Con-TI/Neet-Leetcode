class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m,n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for nj in range(n):
                        # Mark the affected non 0 entries
                        matrix[i][nj] = -1 if matrix[i][nj] != 0 else 0
                    for ni in range(m):
                        matrix[ni][j] = -1 if matrix[ni][j] != 0 else 0
                    
        for i in range(m):
            for j in range(n):
                matrix[i][j] = 0 if matrix[i][j] == -1 else matrix[i][j]
        