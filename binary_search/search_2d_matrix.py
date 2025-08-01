class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = [num for row in matrix for num in row]        
        l = 0
        r = len(array)-1
        while l<=r:
            m = l+(r-l)//2
            if array[m] == target:
                return True
            elif array[m] < target:
                l = m+1
            else:
                r = m-1
        return False