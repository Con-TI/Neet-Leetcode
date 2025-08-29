class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        
        # Faster than brute force
        n = len(arr)
        if m*k > n:
            return False

        cnt = 0
        # Total number of matches from the below loop
        patt = m*(k-1)
        for i in range(n-m):
            if arr[i] == arr[i+m]:
                cnt += 1
                if cnt == patt:
                    return True
            else:
                cnt = 0
        return False

        # Brute force
        # Idea: go through every possible pattern of size m
        # and see the length
        # Return the best possible length of repeats

        if m >= len(arr) and k > 1:
            return False

        best_repeats = 0

        if m == 1:
            for i in range(0,len(arr)):
                repeats = 1
                pattern = arr[i]
                for j in range(i+1,len(arr)):
                    if arr[j] == pattern:
                        repeats += 1
                    else:
                        break
                best_repeats = max(repeats, best_repeats)
                if best_repeats >= k:
                    return True
        else:
            for i in range(0,len(arr)-m):
                repeats = 1
                pattern = arr[i:i+m]
                for j in range(i+m, len(arr),m):
                    if j+m>len(arr):
                        break
                    if (arr[j:j+m] == pattern):
                        repeats += 1
                    else:
                        break
                best_repeats = max(repeats, best_repeats)
                if best_repeats >= k:
                    return True
        
        return False

