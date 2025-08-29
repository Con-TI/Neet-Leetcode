class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if len(meetings) < n:
            return 0

        count = [0] * n
        available = []
        meetings.sort()

        for i in range(n):
            heapq.heappush(available, (0, i)) # (time, room_id)
        
        for start, end in meetings:
            # Room is available before meeting start 
            # write updated time = start
            # This simulates "waiting" for the meeting to begin
            while available and available[0][0] < start:
                end_time, room = heapq.heappop(available)
                heapq.heappush(available, (start, room))
            
            # Finds the earliest available room
            end_time, room = heapq.heappop(available)
            # Adds it back in as a room only available after the meeting has ended
            heapq.heappush(available, (end_time + (end-start), room))
            count[room] += 1

        return count.index(max(count))