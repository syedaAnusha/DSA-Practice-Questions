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
    # Time Complexity: O(N+E) + O(E*4ɑ) + O(N*(ElogE + E)) 
    # Space Complexity:  O(N)+ O(N) +O(2N) ~ O(N)
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountSize = len(accounts)
        mapMailNodes = {}
        ds = DisjointSet(accountSize)
        for i in range(accountSize):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail not in mapMailNodes:
                    mapMailNodes[mail] = i
                else:
                    ds.unionBySize(i, mapMailNodes[mail])
        
        mergedMails = [[] for _ in range(accountSize)]
        for mail, index in mapMailNodes.items():
            node = ds.findUltimateParent(index)
            mergedMails[node].append(mail)
        
        finalAccounts = []
        for i in range(len(mergedMails)):
            if not mergedMails[i]:
                continue
            mergedMails[i].sort()
            temp = [accounts[i][0]]

            for mail in mergedMails[i]:
                temp.append(mail)
            
            finalAccounts.append(temp)
        
        return finalAccounts    