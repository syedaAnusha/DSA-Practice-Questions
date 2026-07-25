class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n + E)
    # Space Complexity: O(n) + O(n) + O(n) = O(n)
    def dfs(self, node, graph, visited, pathVisited):
        visited[node] = 1
        pathVisited[node] = 1
        for adjacentNode in graph[node]:
            if visited[adjacentNode] == 0:
                if self.dfs(adjacentNode, graph, visited, pathVisited):
                    return True
            elif pathVisited[adjacentNode] == 1:
                return True
        pathVisited[node] = 0

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        totalNodes = len(graph)
        visited = [0 for _ in range(totalNodes)]
        pathVisited = [0 for _ in range(totalNodes)]
        safeNodes = []
        for i in range(totalNodes):
            if visited[i] == 0:
                self.dfs(i, graph, visited, pathVisited)
        
        for i in range(len(pathVisited)):
            if pathVisited[i] == 0:
                safeNodes.append(i)
        return safeNodes       