from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(2*E)
    # Space Complexity: O(2n)
    def bfs(self, adj):
        # code here
        NoOfNodes = len(adj)
        visitedNodes = NoOfNodes*[0]  # 5
        q = deque([0]) # since it is 0 based indexing
        visitedNodes[0] = 1
        bfs = []
        
        while q:
            node = q.popleft()
            bfs.append(node)
            row = node
            for elem in adj[row]:
                if visitedNodes[elem] != 1:
                    visitedNodes[elem] = 1
                    q.append(elem)
        return bfs