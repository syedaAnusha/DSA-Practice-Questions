class DisjointSet:
    # Time Complexity: O(4 alpha) ≈ O(constant Time)
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

class solution:
    ds = DisjointSet(7)
    ds.unionBySize(1,2)
    ds.unionBySize(2,3)
    ds.unionBySize(4,5)
    ds.unionBySize(6,7)
    ds.unionBySize(5,6)
    # check if 3 & 7 have same parent or not
    if ds.findUltimateParent(3) == ds.findUltimateParent(7):
        print('same')
    else:
        print('not same')
    ds.unionBySize(3,7)

    if ds.findUltimateParent(3) == ds.findUltimateParent(7):
        print('same')
    else:
        print('not same')
