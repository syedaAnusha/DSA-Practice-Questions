class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n + E)
    # Space Complexity: O(n) + O(n) + O(n)
    def dfs(self, node, adj, visited, pathVisited):
        visited[node] = 1
        pathVisited[node] = 1
        
        for adjacentNode in adj[node]:
            if visited[adjacentNode] == 0:
                if self.dfs(adjacentNode, adj, visited, pathVisited):
                    return True
            elif pathVisited[adjacentNode] == 1:
                return True
        
        pathVisited[node] = 0  
        return False
            
        
    def getAdjList(self, V,edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            
        return adj
        
    def isCyclic(self, V, edges):
        # code here
        adj = self.getAdjList(V, edges)
        visited = [0] * V
        pathVisited = [0] * V
        
        for i in range(V):
            if visited[i] == 0:
                if self.dfs(i, adj, visited, pathVisited):
                    return True
        return False