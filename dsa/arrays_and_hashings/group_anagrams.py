class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            counts = [0]*26
            for char in s:
                counts[ord(char)-ord('a')] += 1
            ans[tuple(counts)].append(s)
        return list(ans.values())