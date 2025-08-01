class Solution:
    def reorganizeString(self, s: str) -> str:
        # # Frequency count
        # freq = [0] * 26
        # for char in s:
        #     freq[ord(char) - ord('a')] += 1
        
        # max_freq = max(freq)
        # if max_freq > (len(s) + 1) // 2:
        #     return ""
        
        # res = []
        # while len(res) < len(s):
        #     maxIdx = freq.index(max(freq))
        #     char = chr(maxIdx + ord('a'))
        #     res.append(char)
        #     freq[maxIdx] -= 1
        #     if freq[maxIdx] == 0:
        #         continue
            
        #     ## Add next most freq char in same loop
        #     tmp = freq[maxIdx]
        #     freq[maxIdx] = float("-inf")
        #     nextMaxIdx = freq.index(max(freq))
        #     char = chr(nextMaxIdx + ord('a'))
        #     res.append(char)
        #     freq[maxIdx] = tmp
        #     freq[nextMaxIdx] -= 1
        
        # return ''.join(res)

        # Frequency count using a max heap
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        # Max num is lowest freq, so pop drops out the highest freq
        heapq.heapify(maxHeap)
        
        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            # Add to string
            res += char
            # Reduce by 1
            cnt += 1

            # If a previous letter exists
            # add the previous to the maxHeap.
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            # We have a non zero count, 
            # We have a duplicate
            # Assign prev so that it can be added back in the 
            # next iteration        
            if cnt != 0:
                prev = [cnt, char]
        
        return res