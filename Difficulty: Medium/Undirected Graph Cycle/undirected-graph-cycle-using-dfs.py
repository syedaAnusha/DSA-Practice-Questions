from collections import deque
class Solution:
    # Optimal Approach-1
    # Time Complexity: O(V + 2E) + O(V) // this extra O(v) is only for connected components
    # Space Complexity: O(V) + O[V]
    def getAdjacencyList(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        return adj
    
    def dfs(self, startNode, adj, visitedArr, parentNode):
        visitedArr[startNode] = 1
        for adjacentNode in adj[startNode]:
            if visitedArr[adjacentNode] == 0:
                if self.dfs(adjacentNode, adj, visitedArr, [startNode]):
                    return True
            elif adjacentNode != parentNode[0]:
                return True
        return False
        
        
	def isCycle(self, V, edges):
		#Code here
		adj = self.getAdjacencyList(V, edges)
		visitedArr = [0 for _ in range(V)]
		# what if we have connected graphs also
		for i in range(V):
		    if visitedArr[i] == 0:
		        if self.dfs(i, adj, visitedArr, [-1]):
		            return True
		return False
