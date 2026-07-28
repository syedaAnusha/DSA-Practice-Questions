from collections import deque
class Solution:
    # Optimal Approach
    # Time  Complexity: O(n * k)
    # Space  Complexity: O(V)
    def topoSort(self, V, adj):
        indegree = [0] * V

        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1

        q = deque([])
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            node = q.popleft()
            topo.append(node) 
            
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        # Edge case: if there is a cycle in graph
        if len(topo) < V:
            return []
            
        return topo
        
        
    def findAdjList(self, V, N, words, present_chars_set):
        adj = [[] for _ in range(V)]
        
        if N > 0:
            for char in words[0]:
                present_chars_set.add(char)
        
        for i in range(N-1):
            s1, s2 = words[i], words[i+1]
            
            for char in s2:
                present_chars_set.add(char)
                
            
            # Edge case: If s1 is greater than s2
            if len(s1) > len(s2) and s1.startswith(s2):
                return ""
                
            size = min(len(s1), len(s2))
            for j in range(size):
                if s1[j] != s2[j]:
                    adj[ord(s1[j])-ord('a')].append(ord(s2[j])-ord('a'))
                    break
        return adj

    def findOrder(self, words):
        # code here
        V = 26
        N = len(words)
        present_chars_set = set()
        ans = []
        
        adj = self.findAdjList(V, N, words, present_chars_set)
        if not adj:
            return ""
            
        topo = self.topoSort(V, adj)
        if not topo:
            return ""
        
        for i in topo:
            char = chr(i + ord('a'))
            if char in present_chars_set:
                ans.append(char)
                
        return ''.join(ans)