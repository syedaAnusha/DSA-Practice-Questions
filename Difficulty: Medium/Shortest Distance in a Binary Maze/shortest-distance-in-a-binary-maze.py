from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(4*n*m)
    # Space Complexity: O(n*m)
    def isValidCell(self, rows, cols, row, col, mat, distanceMatrix, distance):
        return (row >= 0 and row < rows and
                col >= 0 and col < cols and
                mat[row][col] == 1 and
                (distance + 1) < distanceMatrix[row][col])
                
    def bfs(self, distanceMatrix, mat, que, dest):
        rows = len(mat)
        cols = len(mat[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while que:
            distance, row, col = que.popleft()
            if row == dest[0] and col == dest[1]:
                return distance
            for dr, dc in directions:
                nRow = row + dr
                nCol = col + dc
                if self.isValidCell(rows, cols, nRow, nCol, mat, distanceMatrix, distance):
                    distanceMatrix[nRow][nCol] = distance + 1
                    que.append((distanceMatrix[nRow][nCol], nRow, nCol))
        return -1               

    def shortestPath(self, mat: list[list[int]], src: list[int], dest: list[int]) -> int:
        # code here
        rows = len(mat)
        cols = len(mat[0])
        sRow, sCol = src[0], src[1]
        dRow, dCol = dest[0], dest[1]
        # what if source is equal to destination
        if sRow == dRow and sCol == dCol:
            if mat[sRow][sCol] == 0:
                return -1
            else:
                return 0
        que = deque([(0, sRow, sCol)])
        distanceMat = [[float('inf')]*cols for _ in range(rows)]
        distanceMat[sRow][sCol] = 0 
        return self.bfs(distanceMat, mat, que, dest)