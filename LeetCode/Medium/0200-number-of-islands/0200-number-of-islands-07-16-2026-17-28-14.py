from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(n^2) + O(n*m*4)
    # Space Complexity: O(n^2) + O(n^2)
    def checkValidity(self, row, col, grid, visitedGrid):
        rows = len(grid)
        cols = len(grid[0])
        return (row >= 0 and row < rows and 
                col >= 0 and col < cols and 
                grid[row][col] == "1" and 
                visitedGrid[row][col] == 0)

    def bfs(self, row, col, visitedGrid, grid):
        visitedGrid[row][col] = 1
        q = deque([(row, col)]) 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                neighborRow = row + dr
                neighborCol = col + dc
                if self.checkValidity(neighborRow, neighborCol, grid, visitedGrid):
                        visitedGrid[neighborRow][neighborCol] = 1
                        q.append((neighborRow, neighborCol))
            
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visitedGrid = [[0] * cols for _ in range(rows)]
        numberOfIslands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and visitedGrid[row][col] == 0:
                    numberOfIslands += 1
                    self.bfs(row, col, visitedGrid, grid) 

        return numberOfIslands; 