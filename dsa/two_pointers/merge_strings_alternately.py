class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        limit = min(len(word1), len(word2))
        i = 0
        j = 0
        while i<limit and j<limit:
            res += word1[i]            
            i+=1 
            res += word2[j]
            j+=1 
        if len(word1) > limit:
            res += word1[i:]
        if len(word2) > limit:
            res += word2[i:]
        return res    