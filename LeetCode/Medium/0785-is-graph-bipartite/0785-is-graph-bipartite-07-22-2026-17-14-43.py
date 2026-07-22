from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n + 2E)
    # Space Complexity: O(n) + O(n)
    def bfs(self, node, color, graph, visitedColoredNodes):
        q = deque([node])
        visitedColoredNodes[node] = color
        while q:
            curNode = q.popleft()
            for node in graph[curNode]:
                if visitedColoredNodes[node] == -1:
                    if visitedColoredNodes[curNode] == 0:
                        visitedColoredNodes[node] = 1
                    else:
                        visitedColoredNodes[node] = 0
                    q.append(node)
                elif visitedColoredNodes[node] == visitedColoredNodes[curNode]:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        totalNodes = len(graph)
        visitedColoredNodes = [-1] * totalNodes
        for i in range(totalNodes):
            if visitedColoredNodes[i] == -1:
                if not self.bfs(i, 0, graph, visitedColoredNodes):
                    return False
        return True