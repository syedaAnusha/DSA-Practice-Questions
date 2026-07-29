from typing import List
class Solution:
    # Optimal Approach
    # Time Complexity: O(n) + O(n + E) + O(n + E)
    # Space Complexity: O(n) + O(n) = O(n)
    def findShortestPath(self, V, stack, adj, visitedNodes):
        distance = [float('inf') for _ in range(V)]
        distance[0] = 0 # the distance of a source node to itself will always be 0
        
        while stack:
            node = stack.pop()
            if distance[node] != float('inf'):
                for tple in adj[node]:
                    adjacentNode, dist = tple[0], tple[1]
                    adjNodeDist = distance[node] + dist
                    distance[adjacentNode] = min(distance[adjacentNode], adjNodeDist)
        
        for i in range(V):
            if distance[i] == float('inf'):
                distance[i] = -1
                
                
        return distance
                
    def topoSort(self, node, adj, visitedNodes, stack):
        visitedNodes[node] = 1
        
        for tple in adj[node]:
            adjacentNode = tple[0]
            if visitedNodes[adjacentNode] == 0:  
                self.topoSort(adjacentNode, adj, visitedNodes, stack)
        
        stack.append(node)
        
    def findAdjList(self, V, edges):
        adj = [[] for _ in range(V)]
        
        for u, v, distance in edges:
            tple = (v, distance)
            adj[u].append(tple)
            
        return adj

    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        visitedNodes = [0 for _ in range(V)]
        adj = self.findAdjList(V, edges)
        stack = []
        
        for i in range(V):
            if visitedNodes[i] == 0:
                self.topoSort(i, adj, visitedNodes, stack)
        
        distance = self.findShortestPath(V, stack, adj, visitedNodes)
        return distance