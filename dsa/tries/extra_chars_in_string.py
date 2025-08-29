class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        # Recursion
        words = set(dictionary)

        # Runs dfs to return smallest num of leftover words
        def dfs(i):
            if i == len(s):
                return 0
            res = 1 + dfs(i+1) # Skips current character and adds it to default result
            
            # For any prefix/substring starting from i
            # Check if said substring is in the dictionary
            # If it is, we check 
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    # We know that considering the subproblem i to len(s)
                    # that i to j+1 is a valid substring
                    # So the minimum of starting from j+1 instead and 
                    # the current default is our result for solving
                    # the subproblem
                    res = min(res, dfs(j+1))
                
            # res is the answer to the subproblem if our string were s[i:]
            return res

        return dfs(0)
        """
        # Dynamic programming top-down 
        # Start from the whole string
        """
        dp = {len(s) : 0}

        def dfs(i):
            if i in dp:
                return dp[i]

            # Skip current character
            res = 1 + dfs(i+1)

            for word in dictionary:
                # Quick discard if the word can't fit in the remaining suffix
                if i + len(word) > len(s):
                    continue


                flag = True
                for j in range(len(word)):
                    # If there is a letter mismatch
                    # Then the word does not match any
                    # prefix of the current substring
                    if s[i + j] != word[j]:
                        flag = False
                        break
                # If the word had matched we do the minimum thing
                if flag:
                    res = min(res, dfs(i + len(word)))
            # Update the dictionary for the results
            dp[i] = res
            return res

        return dfs(0)
        """

        # Dynamic programming bottom up (i.e. not via recursive stack)
        """n = len(s)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            dp[i] = 1 + dp[i+1]
            for word in dictionary:
                if i+len(word) <= n and s[i:i + len(word)] == word:
                    dp[i] = min(dp[i], dp[i+len(word)])

        return dp[0] """
        # Dynamic programming with a trie top down
        """
        trie = Trie()
        for w in dictionary:
            trie.addWord(w)
        
        dp = {len(s):0}

        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i+1)
            curr = trie.root
            for j in range(i, len(s)):
                # No such matching prefix in the substring
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                # If the word exists as a prefix to the current substring
                if curr.isWord:
                    res = min(res, dfs(j+1))
            dp[i] = res
            return res

        return dfs(0)
        """
        # Dynamic programming with a trie bottom up
        trie = Trie()
        for w in dictionary:
            trie.addWord(w)

        n = len(s)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            curr = trie.root
            for j in range(i, len(s)):
                # No such matching prefix in the substring
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                # If the word exists as a prefix to the current substring
                if curr.isWord:
                    dp[i] = min(dp[i], dp[j+1])

        return dp[0]
