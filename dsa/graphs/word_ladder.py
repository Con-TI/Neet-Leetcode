class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = {word : set() for word in wordList}
        graph[beginWord] = set()
        # Construct the graph
        for word1 in graph:
            for word2 in wordList:
                if self.differ_by_one(word1, word2):
                    graph[word1].add(word2)
                    graph[word2].add(word1)        
        
        # Perform BFS
        visit = set()
        q = deque([beginWord])
        flag = False
        height = 1
        while q:
            height += 1
            for _ in range(len(q)):
                node = q.popleft()
                visit.add(node)
                for nei in graph[node]:
                    if nei not in visit:
                        q.append(nei)
                    if nei == endWord:
                        flag = True
                        break
                if flag:
                    break
            if flag:
                break
            
        if not flag:
            return 0
        return height


    def differ_by_one(self, word1, word2):
        ptr = 0
        counter = 0
        while ptr < len(word1):
            if word1[ptr] != word2[ptr]:
                counter += 1
            if counter > 1:
                break        
            ptr += 1
        if counter != 1:
            return False
        return True