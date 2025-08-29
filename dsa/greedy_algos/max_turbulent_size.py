class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        res = cnt = 0
        # Start with no sign
        sign = -1

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                # Only add to the count if sign flips
                # Otherwise assume its a reset to 1 change
                cnt = cnt + 1 if sign == 0 else 1
                sign = 1
            elif arr[i] < arr[i+1]:
                # Only add to the count if sign flips
                # Otherwise assume its a reset to 1 change
                cnt = cnt + 1 if sign == 1 else 1
                sign = 0
            else:
                # Stagnant, reset count
                cnt = 0
                sign = -1
        
            res = max(res, cnt)
        
        return res + 1