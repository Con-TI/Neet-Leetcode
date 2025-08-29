class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Maxheap (uses a queue for cooldown)
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

        # Greedy ()

        ## Count letters
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        ## Sort array in order of frequency    
        count.sort()
        maxf = count[-1]
        ## Total idle time from most freq letter 
        # (E.g. n=2, A is the most frequent, A _ _ A _ _ A ...)
        # (In each "idle gap" you can only have one type of each task)
        idle = (maxf - 1)*n

        ## Fill idle slots with other letters
        for i in range(24, -1, -1):
            # At most maxf - 1 slots can be used
            # count[i] could have at most maxf by the sorting
            idle -= min(maxf - 1, count[i])

        # Add length of tasks to account for time step for each one
        return max(0, idle) + len(tasks)

        # Math

        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        ## Consider only the highest frequency stuff
        maxf = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxf else 0

        ## Add the idle time and extra time for each maxf task
        ## E.g. if A =3, then it adds _ _ A _ _ A
        ## maxCount then adds 1 for the start
        ## E.g. if A = B = 3, then it adds _ _ A _ _ A
        ## maxCount then adds 2 so that we get A B _ A B _ A B
        ## Consider maxCount > n, then we definitely have no idle time.

        time = (maxf - 1) * (n + 1) + maxCount

        ## We consider len(tasks) due to the presence of lower frequency stuff
        ## E.g. A = 3 B = 3 C = D = E = F = 1
        ## Since they are different the ones can be done in consecutive order.
        return max(len(tasks), time)

