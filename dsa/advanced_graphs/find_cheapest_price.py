class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        # Dijkstra's
        """
        edges = defaultdict(list)
        for from_i,to_i, price_i in flights:
            edges[from_i].append([to_i,price_i])

        minHeap = [(0, -1, src)] # (total price, stops, airport)
        visit = set()

        while minHeap:
            print(minHeap, visit)
            total_price, num_stops, airport = heapq.heappop(minHeap)     
            if (airport, num_stops) in visit or num_stops > k:
                continue
            if airport == dst:
                return total_price
            visit.add((airport,num_stops))

            for nei, p in edges[airport]:
                heapq.heappush(minHeap,(total_price + p, num_stops + 1, nei))

        return -1
        """

        # SPFA
        """
        prices = [float('inf')] * n
        prices[src] = 0
        edges = defaultdict(list)
        for u, v, p in flights:
            edges[u].append((v,p))

        q = deque([(0, 0, src)])


        while q:
            total_price, num_stops, node = q.popleft()
            if num_stops > k:
                continue

            for nei, p in edges[node]:
                if total_price + p < prices[nei]:
                    # Update with better distance
                    prices[nei] = total_price + p
                    q.append((total_price + p,num_stops + 1, nei))

        
        return prices[dst] if prices[dst] != float('inf') else -1
        """
