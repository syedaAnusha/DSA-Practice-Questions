from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(E) = flights size
    # Space Complexity: O(V)
    def findAdjList(self, n, flights):
        adj = [[] for _ in range(n)]
        for loc1, loc2, price in flights:
            adj[loc1].append((loc2, price))
        return adj
    
    def bfs(self, adj, dest, k, distanceArr, q):
        while q:
            stops, node, distance = q.popleft()
            if stops > k:
                continue
            for tple in adj[node]:
                adjNode = tple[0]
                edgeWeight = tple[1]
                adjDist = distance + edgeWeight
                if adjDist < distanceArr[adjNode] and stops <= k:
                    distanceArr[adjNode] = adjDist
                    q.append((stops+1, adjNode, adjDist))

        if distanceArr[dest] == float('inf'):
            return -1
        return distanceArr[dest] 

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = self.findAdjList(n, flights)
        distance = [float('inf')] * n
        distance[src] = 0
        que = deque([])
        que.append((0, src, 0))
        return self.bfs(adj, dst, k, distance, que)        