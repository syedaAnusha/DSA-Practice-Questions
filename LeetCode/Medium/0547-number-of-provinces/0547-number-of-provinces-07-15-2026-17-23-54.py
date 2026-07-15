class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n + 2E)
    # Space Complexity: O(n) + O(n)
    def getAdjList(self, isConnected):
        adj = [[]]
        for lst in isConnected:
            tempArr = []
            for i in range(len(lst)):
                if lst[i] == 1:
                    tempArr.append(i+1)
            adj.append(tempArr)
        return adj
                     
    def dfs(self, node, visitedNodesArr, adj):
        visitedNodesArr[node] = 1
        for elem in adj[node]:
            if visitedNodesArr[elem] != 1:
                self.dfs(elem, visitedNodesArr, adj)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numOfNodes = len(isConnected)
        visitedNodes = (numOfNodes+1) * [0]
        totalNumOfProvinces = 0
        adj = self.getAdjList(isConnected)

        for i in range(1, numOfNodes+1):
            if visitedNodes[i] != 1:
                self.dfs(i, visitedNodes, adj)
                totalNumOfProvinces += 1

        return totalNumOfProvinces