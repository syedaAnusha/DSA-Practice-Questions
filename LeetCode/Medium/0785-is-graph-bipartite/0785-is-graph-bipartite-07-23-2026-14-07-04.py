class Solution:
    # Optimal Approach using DFS
    # Time Complexity: O(n) + O(n + 2E)
    # Space Complexity: O(n) + O(n)
    def dfs(self, node, color, graph, visitedColoredNodes):
        visitedColoredNodes[node] = color
        for adjacentNode in graph[node]:
                if visitedColoredNodes[adjacentNode] == -1:
                    newColor = int(not color)
                    if not self.dfs(adjacentNode, newColor, graph, visitedColoredNodes):
                        return False
                elif visitedColoredNodes[adjacentNode] == color:
                    return False
            
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        totalNodes = len(graph)
        visitedColoredNodes = [-1] * totalNodes
        for i in range(totalNodes):
            if visitedColoredNodes[i] == -1:
                if not self.dfs(i, 0, graph, visitedColoredNodes):
                    return False
        return True