from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n + 2E)
    # Space Complexity: O(n) + O(n)
    def bfs(self, node, graph, visitedColoredNodes):
        q = deque([node])
        visitedColoredNodes[node] = 0
        while q:
            curNode = q.popleft()
            for adjacentNode in graph[curNode]:
                if visitedColoredNodes[adjacentNode] == -1:
                    visitedColoredNodes[adjacentNode] = int(not visitedColoredNodes[curNode])
                    q.append(adjacentNode)
                elif visitedColoredNodes[adjacentNode] == visitedColoredNodes[curNode]:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        totalNodes = len(graph)
        visitedColoredNodes = [-1] * totalNodes
        for i in range(totalNodes):
            if visitedColoredNodes[i] == -1:
                if not self.bfs(i, graph, visitedColoredNodes):
                    return False
        return True