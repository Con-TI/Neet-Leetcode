class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Sorting and minheap
        n = len(tasks)
        # Unique index for each task
        indices = list(range(n))
        # Sort by enqueue times
        indices.sort(key = lambda i : (tasks[i][0],i))

        class Task:
            def __init__(self, idx):
                self.idx = idx
            
            # Less than operator compares processing times
            def __lt__(self, other):
                if tasks[self.idx][1] != tasks[other.idx][1]:
                    return tasks[self.idx][1] < tasks[other.idx][1]
                return self.idx < other.idx
            
        minHeap = []
        res = []
        time = i = 0
        
        while minHeap or i < n:
            # shift ptr i until the first task where enqueue time is > current time.
            while i < n and tasks[indices[i]][0] <= time:
                heapq.heappush(minHeap,Task(indices[i]))
                i += 1
            
            # If the minheap is empty, then move time to the ith enqueue time
            if not minHeap:
                time = tasks[indices[i]][0]

            # If the minheap is nonempty, 
            # Execute the task and add their processing time
            else:
                next_task = heapq.heappop(minHeap)
                time += tasks[next_task.idx][1]
                res.append(next_task.idx)
            
        return res
