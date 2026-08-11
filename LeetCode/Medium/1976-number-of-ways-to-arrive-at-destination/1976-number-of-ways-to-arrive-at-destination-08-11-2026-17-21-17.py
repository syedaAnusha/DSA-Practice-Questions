import heapq
class Solution:
    # Optimal Approach
    # Time Complexity: O(E log V)
    # Space Complexity: O(V) + O(V)
    def findAdjList(self, n, roads):
        adj = [[] for _ in range(n)]
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))
        return adj
    
    def bfs(self, pq, distance, ways, roads, adj, mod):
        while pq:
            dist, node = heapq.heappop(pq)
            for adjNode, edgeWeight in adj[node]:
                if dist + edgeWeight < distance[adjNode]:
                    distance[adjNode] = dist + edgeWeight
                    ways[adjNode] = ways[node]
                    heapq.heappush(pq, (distance[adjNode], adjNode))
                elif dist + edgeWeight == distance[adjNode]:
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = self.findAdjList(n, roads)
        mod = int(1e9 + 7)
        distance = [float('inf') for _ in range(n)]
        ways = [0 for _ in range(n)]
        src, dest = 0, n-1
        pq = []
        distance[src] = 0
        ways[src] = 1
        heapq.heappush(pq, (distance[src], src))
        self.bfs(pq, distance, ways, roads, adj, mod)
        return ways[dest]%mod
