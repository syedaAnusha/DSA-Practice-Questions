class Solution:
    # Brute Force Approach 
    # Time Complexity: O(n^3) + O(n*n)
    # Space Complexity: O(n*n)
    def floydWarshall(self, distanceMat, n):
        rows = cols = n
        INF = float('inf')
        for k in range(n):
            for i in range(rows):
                for j in range(cols):
                    if distanceMat[i][k] != INF and distanceMat[k][j] != INF:
                        distanceMat[i][j] = min(distanceMat[i][j], distanceMat[i][k] + distanceMat[k][j])
        
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distanceMat = [[float('inf')] * n for _ in range(n)]
        for u, v, wt in edges:
            distanceMat[u][v] = wt
            distanceMat[v][u] = wt
        
        for i in range(n):
            distanceMat[i][i] = 0
        
        self.floydWarshall(distanceMat, n)
        
        minNoOfCities = n
        cityNo = -1

        for city in range(n):
            cityCnt = 0
            for adjCity in range(n):
                if distanceMat[city][adjCity] <= distanceThreshold:
                    cityCnt += 1
            if cityCnt <= minNoOfCities:
                minNoOfCities = cityCnt  
                cityNo = city
        
        return cityNo     