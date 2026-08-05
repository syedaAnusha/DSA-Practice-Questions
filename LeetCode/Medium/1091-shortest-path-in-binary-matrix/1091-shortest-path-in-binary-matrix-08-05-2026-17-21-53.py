from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(8*n*m)
    # Space Complexity: O(n*m)
    def isValidCell(self, rows, cols, row, col, mat, distanceMatrix, distance):
        return (row >= 0 and row < rows and
                col >= 0 and col < cols and
                mat[row][col] == 0 and
                (distance + 1) < distanceMatrix[row][col])

    def bfs(self, distanceMatrix, mat, que, dest):
        rows = len(mat)
        cols = len(mat[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1, 1), (1, -1), (-1, -1), (1,1)]
        while que:
            distance, row, col = que.popleft()
            for dr, dc in directions:
                nRow = row + dr
                nCol = col + dc
                if self.isValidCell(rows, cols, nRow, nCol, mat, distanceMatrix, distance):
                    distanceMatrix[nRow][nCol] = distance + 1
                    que.append((distanceMatrix[nRow][nCol], nRow, nCol))    
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sRow, sCol = 0, 0
        dRow, dCol = n-1, n-1
        dest = [dRow, dCol]
        que = deque([(1, sRow, sCol)])
        distanceMat = [[float('inf')]*n for _ in range(n)]
        distanceMat[sRow][sCol] = 1 
        self.bfs(distanceMat, grid, que, dest)
        if distanceMat[dRow][dCol] == float('inf') or grid[sRow][sCol] == 1:
            return -1
        return distanceMat[dRow][dCol]
        