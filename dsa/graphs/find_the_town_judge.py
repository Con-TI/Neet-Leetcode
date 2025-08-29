class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        track = [0]*n
        
        for a,b in trust:
            track[a-1] -= 1
            track[b-1] += 1

        for num,i in enumerate(track):
            if i == n-1:
                return num+1

        return -1 