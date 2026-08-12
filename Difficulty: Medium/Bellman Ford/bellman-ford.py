class Solution:
    # Optimal Approach
    # Time Complexity: O(V*E)
    # Time Complexity: O(V)
    def bellmanFord(self, V: int, edges: list[list[int]], src: int) -> list[int]:
        #code here
        INF =  int(1e8)
        distance = [INF for _ in range(V)]
        distance[src] = 0
        
        for _ in range(V-1):
            for u, v, wt in edges:
                if distance[u] != INF and distance[u] + wt < distance[v]:
                    distance[v] = distance[u] + wt
        
        # Nth iteration to check if graph have any negative cycle
        for u, v, wt in edges:
            if distance[u] != INF and distance[u] + wt < distance[v]:
                return [-1]
        
        return distance