class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(2*E)
    # Space Complexity: O(n) + O(n) + O(n) 
    def helperDFS(self, adj, visitedArr, dfs, node):
        visitedArr[node] = 1
        dfs.append(node)
        for elem in adj[node]:
            if visitedArr[elem] != 1:
                self.helperDFS(adj, visitedArr, dfs, elem)
        
    def dfs(self, adj):
        # code here
        numOfNodes = len(adj)
        visitedNodes = numOfNodes * [0]
        dfs = []
        self.helperDFS(adj, visitedNodes, dfs, 0)
        return dfs