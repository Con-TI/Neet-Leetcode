class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map_1 = dict({})
        for letter in s:
            if hash_map_1.get(letter) is None:
                hash_map_1[letter] = 1
            else:
                hash_map_1[letter] += 1

        hash_map_2 = dict({})
        for letter in t:
            if hash_map_2.get(letter) is None:
                hash_map_2[letter] = 1
            else:
                hash_map_2[letter] += 1

        for letter in hash_map_1:
            if hash_map_1.get(letter)!=hash_map_2.get(letter):
                return False
        return True