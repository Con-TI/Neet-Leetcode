class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Greedy max heap (concept: max heap keeps track of counts in these problems)
        res = ""
        maxHeap = []
        for count, char in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
        
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            # If the prior two chars in res are the same
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
                heapq.heappush(maxHeap, (count,char))
            else:
                res += char
                count += 1
                if count:
                    heapq.heappush(maxHeap, (count, char))
        
        return res
