class DisjointSet:
    rank = []
    parent = []
    size = []
    def __init__(self, n):
        self.rank = [0] * (n+1) 
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]

    def findUltimateParent(self, node):
        if node == self.parent[node]:
            return node
        # path compression
        self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        pu = self.findUltimateParent(u)
        pv = self.findUltimateParent(v)
        if pu == pv:
            return 
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

    def unionBySize(self, u, v):
        pu = self.findUltimateParent(u)
        pv = self.findUltimateParent(v)
        if pu == pv:
            return
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

class Solution:
    # Optimal Approach
    # Time Complexity: O(V^2) + O(V)
    # Space Complexity: O(V)
    def countConnected(self, V, edges):
        # code here 
        cntComponents = 0
        ds = DisjointSet(V)
        for u,v in edges:
            ds.unionBySize(u, v)
        
        for i in range(V):
            if ds.parent[i] == i:
                cntComponents += 1
                
        return cntComponents