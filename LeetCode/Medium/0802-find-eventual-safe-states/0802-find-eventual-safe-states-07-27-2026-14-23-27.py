from collections import deque
class Solution:
    # Optimal Approach using topological sort (BFS)
    # Time Complexity: O(n + E) + O(n log n)
    # Space Complexity: O(n) + O(n) + O(n) = O(n)
    def bfs(self, q, adj, indegree):
        safeNodes = []
        while q:
            node = q.popleft()
            safeNodes.append(node)
            for adjNode in adj[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    q.append(adjNode)
        return safeNodes
    
    def findAdjList(self, V, graph, indegree):
        adj = [[] for _ in range(V)]
        for i in range(V):
            for adjNode in graph[i]:
                adj[adjNode].append(i)
                indegree[i] += 1  
        return adj

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        indegree = [0 for _ in range(V)]
        adj = self.findAdjList(V, graph, indegree)
        que = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                que.append(i)

        safeNodes = self.bfs(que, adj, indegree) 
        return sorted(safeNodes)