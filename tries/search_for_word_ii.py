class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        # Brute force backtrack
        ROWS, COLS = len(board), len(board[0])
        res = []
        def backtrack(r,c,i):
            if i==len(word):
                return True
            if (r<0 or c<0 or r>=ROWS or c>=COLS or board[r][c] != word[i]):
                return False

            board[r][c] = '*'
            ret = (backtrack(r+1, c, i+1) 
            or backtrack(r-1, c, i+1) 
            or backtrack(r, c+1, i+1)
            or backtrack(r, c-1, i+1))
            board[r][c] = word[i]
            return ret
        
        # For every word, check strating from every i,j in the matrix
        # If it works append to res and move on
        for word in words:
            flag = False
            for r in range(ROWS):
                if flag:
                    break
                for c in range(COLS):
                    if board[r][c] != word[0]:
                        continue
                    if backtrack(r,c,0):
                        res.append(word)
                        flag = True
                        break
        return res
        """

        # Backtracking using trie
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        # res is now a set since we are searching for all words in one go
        # through the whole grid, so repeats can happen
        res, visit = set(), set()

        # We traverse a trie instead of going brute per word
        # This way whenever any word matches we add it 
        # And we don't do the whole loop with every word
        # Helps when a lot of prefixes match
        def dfs(r, c, node, word):
            if (r<0 or c<0 
            or r>=ROWS or c>=COLS
            or (r,c) in visit
            or board[r][c] not in node.children):
                return

            visit.add((r,c))

            node = node.children[board[r][c]]
            # word is the running word
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root, "")
        
        return list(res)