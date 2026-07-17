from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(n^2) + O(n*m*4)
    # Space Complexity: O(n^2) + O(n*m)
    def putAllRottenOrangesIntoQue(self, grid, visitedGrid, que):
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    visitedGrid[row][col] = 2
                    que.append((row, col, 0))
                elif grid[row][col] == 1:
                    self.cntFreshOranges += 1

    def checkValidity(self, row, col, grid, visitedGrid):
        rows = len(grid)
        cols = len(grid[0])
        return (row >= 0 and row < rows and
                col >= 0 and col < cols and 
                grid[row][col] == 1 and
                visitedGrid[row][col] != 2)

    def bfs(self, grid, visitedGrid):
        que = deque([])
        cntNewRottenOranges = 0
        self.putAllRottenOrangesIntoQue(grid, visitedGrid, que)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while que:
            row, col, time = que.popleft()            
            for dr, dc in directions:
                nRow = row + dr
                nCol = col + dc
                if self.checkValidity(nRow, nCol, grid, visitedGrid):
                    visitedGrid[nRow][nCol] = 2
                    que.append((nRow, nCol, time+1))
                    cntNewRottenOranges += 1

            self.minTime = max(self.minTime, time)
        
        if cntNewRottenOranges != self.cntFreshOranges:
            self.minTime = -1


    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visitedGrid = [[0] * cols for _ in range(rows)]
        self.minTime = 0
        self.cntFreshOranges = 0
        self.bfs(grid, visitedGrid)
        return self.minTime