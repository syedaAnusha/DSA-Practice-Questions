import heapq
class Solution:
    # Optimal Approach
    # Time Complexity: O(E log E) + O(E log E)
    # Space Complexity: O(E)
    def findAdjList(self, V, edges):
        adj = [[] for _ in range(V)]
        
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
            
        return adj
    
    def prims(self, pq, adj, visitedNodes):
        Sum = 0
        while pq:
            wt, node = heapq.heappop(pq)
            if visitedNodes[node] == 1:
                continue
            visitedNodes[node] = 1
            Sum += wt
            for adjNode, adjWt in adj[node]:
                if visitedNodes[adjNode] == 0:
                    heapq.heappush(pq, (adjWt, adjNode))
        return Sum
                    
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        # code here
        pq = []
        adj = self.findAdjList(V, edges)
        node = 0
        wt = 0
        heapq.heappush(pq, (wt, node))
        visitedNodes = [0 for _ in range(V)]
        return self.prims(pq, adj, visitedNodes)