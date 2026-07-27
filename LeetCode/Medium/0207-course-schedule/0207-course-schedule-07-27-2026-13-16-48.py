from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(n + E)
    # Space Complexity: O(n)
    def findAdjList(self, V, edges, indegree):
        adj = [[] for _ in range(V)]
        for a, b in edges:
            adj[b].append(a)
            indegree[a] += 1

        return adj
    
    def bfs(self, q, adj, indegree):
        topoCnt = 0
        while q:
            node = q.popleft()
            topoCnt += 1
            for adjNode in adj[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    q.append(adjNode)

        return topoCnt

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        adj = self.findAdjList(numCourses, prerequisites, indegree)
        que = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                que.append(i)

        topoCnt = self.bfs(que, adj, indegree)
        if topoCnt < numCourses:
            return False
        return True      