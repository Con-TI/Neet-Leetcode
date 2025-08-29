class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = defaultdict(int)
        for c in s1:
            s1_counts[c] += 1
        n = len(s1)
        for i in range(len(s2)-n+1):
            s2_counts = defaultdict(int)
            for c in s2[i:i+n]:
                s2_counts[c] += 1
            if s1_counts == s2_counts:
                return True
        return False