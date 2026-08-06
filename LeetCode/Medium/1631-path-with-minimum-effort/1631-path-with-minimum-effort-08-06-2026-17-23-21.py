import heapq
class Solution:
    # Optimal Approach
    # Time Complexity: O(4*n*m * log(n*m))
    # Space Complexity: O(n*m)
    def isMinimumHeight(self, row, col, heights):
        rows = len(heights)
        cols = len(heights[0])
        return (row >= 0 and row < rows and
                col >= 0 and col < cols)

    def bfs(self, pq, heights, minHeights, destRow, destCol):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while pq:
            difference, row, col = heapq.heappop(pq)
            if row == destRow and col == destCol:
                return difference

            for dr, dc in directions:
                nrow = dr + row
                ncol = dc + col
                if self.isMinimumHeight(nrow, ncol, heights):
                    newEffort = max(abs(heights[row][col] - heights[nrow][ncol]), difference)
                    if newEffort < minHeights[nrow][ncol]:
                        heapq.heappush(pq, (newEffort, nrow, ncol))
                        minHeights[nrow][ncol] = newEffort

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq = []
        rows = len(heights)
        cols = len(heights[0])
        sr, sc = 0, 0
        dr, dc = rows-1, cols-1
        minHeights = [[float('inf')]*cols for _ in range(rows)]
        minHeights[sr][sc] = 0
        heapq.heappush(pq, (0, sr, sc))
        return self.bfs(pq, heights, minHeights, dr, dc)
