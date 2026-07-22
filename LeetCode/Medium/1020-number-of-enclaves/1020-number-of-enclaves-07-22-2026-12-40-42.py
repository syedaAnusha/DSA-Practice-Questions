class Solution:
    # Optimal Approach
    # Time Complexity: O(n*m) + O(n*m*4)
    # Space Complexity: O(n*m) + O(n*m)
    def isValidCell(self, row, col, grid, visitedGrid):
        rows = len(grid) 
        cols = len(grid[0])
        return (row >= 0 and row < rows and
                col >= 0 and col < cols and
                grid[row][col] == 1 and
                visitedGrid[row][col] == 0)

    def dfs(self, row, col, grid, visitedGrid):
        visitedGrid[row][col] = 1
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dr, dc in directions:
            nRow = dr + row
            nCol = dc + col
            if self.isValidCell(nRow, nCol, grid, visitedGrid):
                self.dfs(nRow, nCol, grid, visitedGrid)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visitedGrid = [[0]*cols for _ in range(rows)]
        numberOfLands = 0

        # for first and last row
        for col in range(cols):
            if grid[0][col] == 1 and visitedGrid[0][col] == 0:
                self.dfs(0, col, grid, visitedGrid)
            
            if grid[rows-1][col] == 1 and visitedGrid[rows-1][col] == 0:
                self.dfs(rows-1, col, grid, visitedGrid)
        
        # for first and last col
        for row in range(rows):
            if grid[row][0] == 1 and visitedGrid[row][0] == 0:
                self.dfs(row, 0, grid, visitedGrid)
            
            if grid[row][cols-1] == 1 and visitedGrid[row][cols-1] == 0:
                self.dfs(row, cols-1, grid, visitedGrid)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and visitedGrid[row][col] == 0:
                    numberOfLands += 1

        return numberOfLands