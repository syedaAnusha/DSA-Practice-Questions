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
    
    def bfs(self, startNode, adj, visitedArr):
        visitedArr[startNode] = 1
        q = deque([(startNode, -1)])
        
        while q:
            node, source = q.popleft()
            for neighborNode in adj[node]:
                if visitedArr[neighborNode] == 0:
                    visitedArr[neighborNode] = 1
                    q.append((neighborNode, node))
                elif source != neighborNode:
                    return True
        return False
        
	def isCycle(self, V, edges):
		#Code here
		adj = self.getAdjacencyList(V, edges)
		visitedArr = [0 for _ in range(V)]
		# what if we have connected graphs also
		for i in range(V):
		    if visitedArr[i] == 0:
		        if self.bfs(i, adj, visitedArr):
		            return True
		return False