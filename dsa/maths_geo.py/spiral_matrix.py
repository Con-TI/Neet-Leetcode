class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, n-1
        t, d = 0, m-1

        res = []
        # Traverse a circle
        while l<r and t<d:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            for j in range(t+1,d+1):
                res.append(matrix[j][r])
            for i in range(r-1,l-1,-1):
                res.append(matrix[d][i])
            for j in range(d-1,t,-1):
                res.append(matrix[j][l])
            
            l+=1
            r-=1
            t+=1
            d-=1

        print(l,r,t,d)

        if t<d and l == r:
            for j in range(t,d+1):
                res.append(matrix[j][r])
        elif l<r and t == d:
            for i in range(l,r+1):
                res.append(matrix[t][i])
        elif t == d and l == r:
            res.append(matrix[t][l])

        return res


