class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
    
        res = [0,0,0]
        for trip in triplets:
            # If trip can fit then it exists in one of the solutions
            if all([trip[i] <= target[i] for i in range(3)]):
                res = [max(res[i],trip[i]) for i in range(3)]

        return res == target
