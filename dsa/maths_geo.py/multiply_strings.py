class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"

        res = [0] * (len(num1) + len(num2)) 
        # Reverse
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                # Add and carryover
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10
        
        # Reverse again
        res, leading_zeroes = res[::-1], 0
        # Find the first non zero digit
        while leading_zeroes < len(res) and res[leading_zeroes] == 0:
            leading_zeroes += 1
        
        # map applies str to every item in truncated res
        res = map(str, res[leading_zeroes:])
        return "".join(res)
