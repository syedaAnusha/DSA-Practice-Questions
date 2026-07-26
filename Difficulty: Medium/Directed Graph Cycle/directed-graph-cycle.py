from collections import deque
class Solution:
    # Optimal Approach using BFS (kahn's algorithm)
    # Time Complexity: O(n + E)
    # Space Complexity: O(n) 
    def bfs(self, que, indegree, adj):
        topoCnt = 0
        
        while que:
            node = que.popleft()
            topoCnt += 1
            
            for adjNode in adj[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    que.append(adjNode)
        return topoCnt
    
    def findAdjacentAndIndegreeOfAdjacentNodes(self, V, edges, indegree):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        return adj
        
    def isCyclic(self, V, edges):
        # code here
        indegree = [0 for _ in range(V)]
        adj = self.findAdjacentAndIndegreeOfAdjacentNodes(V, edges, indegree)
        que = deque([])
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                que.append(i)
                
        topoCnt = self.bfs(que, indegree, adj) 
        if  topoCnt ==  V:
            return False
        return True