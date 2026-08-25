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
    # Optimal Approach Using Kruskal's Algorithm
    # Time Complexity: O(E) + O(E log E) + O(E * 4*alpha*2)
    # Space Complexity: O(2V) + O(E)
    def sortAllEdgesByWeight(self, edges):
        Edges = []
        for u,v,w in edges:
            Edges.append((w,u,v))
            
        sortedEdges = sorted(Edges)
        return sortedEdges
        
    def kruskal(self, edges, ds):
        MSTSum = 0
        for weight, u, v in edges:
            if ds.findUltimateParent(u) != ds.findUltimateParent(v):
                MSTSum += weight
                ds.unionBySize(u, v) 
                
        return MSTSum
                    
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        # code here
        sortedEdgesByWeight = self.sortAllEdgesByWeight(edges)
        ds = DisjointSet(V)
        return self.kruskal(sortedEdgesByWeight, ds)
        