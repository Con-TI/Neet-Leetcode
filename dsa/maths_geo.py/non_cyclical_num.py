class Solution:
    def isHappy(self, n: int) -> bool:
        
        def next_num(k):
            num = 0
            while k:
                num += (k%10)**2
                k = k//10
            return num

        visit = set()
        while next_num(n) not in visit:
            n = next_num(n)
            visit.add(n)
        
        return True if n == 1 else False
