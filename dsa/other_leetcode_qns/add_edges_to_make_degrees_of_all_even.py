class Solution(object):
    def isPossible(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Idea: 
        # If there's an odd fully connected node, false
        # If there are more than 4 odd nodes, false
        # If there are an odd number of odd nodes, false

        # In the case that we have either 2 or 4 odd nodes:
        # For 2, check if they are already connected. If yes then search every non adjacent node and see if they work as an intermediate, otherwise true
        # For 4, check if there is a way to make 2 pairs of unconnected nodes. If yes, True,
        # else False
        
        degree = [0 for _ in range(n+1)]
        adjacency = [[]for _ in range(n+1)]
        odd_nodes = []

        for a,b in edges:
            degree[a] += 1
            adjacency[a].append(b)
            degree[b] += 1
            adjacency[b].append(a)

        odd_counts = 0        

        for i,deg in enumerate(degree[1:]):
            if deg == (n-1) and deg % 2 == 1:
                    return False

            if deg%2 == 1:
                odd_counts += 1
                odd_nodes.append(i+1)

        if odd_counts % 2 == 1:
            return False
        elif odd_counts > 4:
            return False
        else:
            # Now we have 0, 2 or 4 nodes.
            if odd_counts == 0:
                return True
            elif odd_counts == 2:
                if odd_nodes[1] not in adjacency[odd_nodes[0]]:
                    return True
                
                for i in range(1,n+1):
                    if (i not in adjacency[odd_nodes[0]]) and (i not in adjacency[odd_nodes[1]]):
                        return True

                return False
            else:
                pairs = [set([odd_nodes[0], odd_nodes[i]]) for i in range(1,4)]
                odd_nodes = set(odd_nodes)
                for pair1 in pairs:
                    pair2 =  odd_nodes - pair1
                    x,y = pair1
                    w,z = pair2
                    if y not in adjacency[x] and w not in adjacency[z]:
                        return True
                return False