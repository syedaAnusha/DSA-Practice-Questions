class Solution:
    # Optimal Approach using DFS
    # Time Complexity: O(n) + O(n + E)
    # Space Complexity: O(n) + O(n)
    def dfs(self, node, adj, visited, st):
        visited[node] = 1
        
        for adjNode in adj[node]:
            if visited[adjNode] == 0:
                self.dfs(adjNode, adj, visited, st)
        
        st.append(node)
                
    def findAdjNodes(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        return adj
        
    def topoSort(self, V, edges):
        # Code here
        adj = self.findAdjNodes(V, edges)
        visited = [0 for _ in range(V)]
        st = []
        for i in range(V):
            if visited[i] == 0:
                self.dfs(i, adj, visited, st)
        return st[::-1]
