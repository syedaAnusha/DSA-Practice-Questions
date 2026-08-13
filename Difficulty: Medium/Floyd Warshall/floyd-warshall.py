class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^3)
    # Space Complexity:O(n^2)
	def floydWarshall(self, dist):
		#Code here
		K = rows = len(dist)
		cols = len(dist[0])
		INF = int(1e8)
        
        for k in range(K):
            for i in range(rows):
                for j in range(cols):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])