import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    # Optimal Approach - 01 using PQ
    # Time Complexity: O(E log V)
    # Space Complexity: O(log V) 
    def findAdjList(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        return adj
    
    def bfs(self, adj, src, minHeap, distance):
        while minHeap:
            dist, node =  heapq.heappop(minHeap)
            if dist > distance[node]:
                continue
            for tple in adj[node]:
                adjNode = tple[0]
                edgeWeight = tple[1]
                if dist + edgeWeight < distance[adjNode]:
                    distance[adjNode] = dist + edgeWeight
                    heapq.heappush(minHeap, (distance[adjNode], adjNode))
        
    def dijkstra(self, V, edges, src):
        # code here
        minHeap = []
        adj = self.findAdjList(V, edges)
        distance = [float('inf')] * V
        distance[src] = 0
        heapq.heappush(minHeap, (distance[src], src))
        self.bfs(adj, src, minHeap, distance)
        return distance