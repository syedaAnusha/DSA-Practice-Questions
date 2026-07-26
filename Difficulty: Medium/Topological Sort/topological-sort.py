from collections import deque
class Solution:
    # Optimal Approach using BFS (kahn's algorithm)
    # Time Complexity: O(n + E)
    # Space Complexity: O(n) + O(n)
    def bfs(self, que, indegree, adj):
        topo = []
        
        while que:
            node = que.popleft()
            topo.append(node)
            
            for adjNode in adj[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    que.append(adjNode)
        return topo


    def findAdjacentAndIndegreeOfAdjacentNodes(self, V, edges, indegree):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        return adj
        
    def topoSort(self, V, edges):
        # Code here
        indegree = [0 for _ in range(V)]
        adj = self.findAdjacentAndIndegreeOfAdjacentNodes(V, edges, indegree)
        que = deque([])
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                que.append(i)
                
        return self.bfs(que, indegree, adj)