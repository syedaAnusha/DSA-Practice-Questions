class Solution:
    # Optimal Approach
    # Time Complexity: O(n*m) + O(n*m*4)
    # Space Complexity: O(n*m)
    def isValidCell(self, row, col, grid, visitedGrid):
        rows = len(grid)
        cols = len(grid[0])
        return (row >= 0 and row < rows and
                col >= 0 and col < cols and 
                grid[row][col] == 'L' and
                visitedGrid[row][col] == 0)
        
    def dfs(self, row, col, grid, visitedGrid, baseIsland, islands):
        visitedGrid[row][col] = 1
        res = (row-baseIsland[0], col-baseIsland[1])
        islands.append(res)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dr, dc in directions:
            nrow = row + dr
            ncol = col + dc
            if self.isValidCell(nrow, ncol, grid, visitedGrid):
                self.dfs(nrow, ncol, grid, visitedGrid, baseIsland, islands)
            
    def countDistinctIslands(self, grid):
        # code here
        rows = len(grid)
        cols = len(grid[0])
        visitedGrid = [[0]*cols for _ in range(rows)]
        setOfDistinctIslands = set()
        
        for row in range(rows):
            for col in range(cols):
                islands = []
                if grid[row][col] == 'L' and visitedGrid[row][col] == 0:
                    self.dfs(row, col, grid, visitedGrid, (row, col), islands)
                    setOfDistinctIslands.add(tuple(islands))
                
        
        return len(setOfDistinctIslands)