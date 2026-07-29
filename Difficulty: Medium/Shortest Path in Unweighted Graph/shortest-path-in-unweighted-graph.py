from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(n + 2E)
    # Space Complexity: O(n) + O(n)
    def findAdjList(self, V, edges):
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        return adj
    
    def bfs(self, adj, q, distance, dest):
        while q:
            node, dist = q.popleft()
            if node == dest:
                return dist
                
            for adjacentNode in adj[node]:
                if dist + 1 < distance[adjacentNode]:
                    distance[adjacentNode] = dist + 1
                    q.append((adjacentNode, distance[adjacentNode]))
        
        return -1
        
        
    def shortestPath(self, V, edges, src, dest):
        # code here
        adj = self.findAdjList(V, edges)
        distance = [float('inf') for _ in range(V)]
        distance[src] = 0
        tple = (src, 0)
        q = deque([tple])
        return self.bfs(adj, q, distance, dest)