import heapq
class Solution:
    # Optimal Approach
    # Time Complexity: O(E log V) + O(V)
    # Space Complexity: O(V) + O(V) + O(v)
    def findAdjList(self, V, edges):
        adj = [[] for _ in range(V+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        return adj
    
    def bfs(self, adj, distance, pq, parentNodes):
        while pq:
            curDist, node = heapq.heappop(pq)
            if curDist > distance[node]:
                continue
                
            for tple in adj[node]:
                adjNode = tple[0]
                edgeWeight = tple[1]
                if curDist + edgeWeight < distance[adjNode]:
                    distance[adjNode] = curDist + edgeWeight
                    heapq.heappush(pq, (distance[adjNode], adjNode))
                    parentNodes[adjNode] = node

        
    def shortestPath(self, V, edges, src, dest):
        # code here
        adj = self.findAdjList(V, edges)
        distance = [float('inf') for _ in range(V+1)]
        distance[src] = 0
        parentNodes = [i for i in range(V+1)]
        pq = []
        path = []
        heapq.heappush(pq, (distance[src], src))
        self.bfs(adj, distance, pq, parentNodes)
        if distance[dest] == float('inf'):
            return [-1]
            
        node = dest
        while parentNodes[node] != node:
            path.append(node)
            node = parentNodes[node]
        
        path.append(node)
        return path[::-1]
