from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(n^2) + O(n*m*4)
    # Space Complexity: O(n*m) + O(n*m)
    def checkValidity(self, row, col, grid, visitedGrid, curColor):
        rows = len(grid)
        cols = len(grid[0])
        return (row >= 0 and row < rows and
                col >= 0 and col < cols and
                grid[row][col] == curColor and
                visitedGrid[row][col] == curColor)

    def bfs(self, row, col, color, grid, visitedGrid):
        curColor = grid[row][col]
        q = deque([(row, col)])
        visitedGrid[row][col] = color
        while q:
            row, col = q.popleft()
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nRow = row + dr
                nCol = col + dc
                if self.checkValidity(nRow, nCol, grid, visitedGrid, curColor):
                    visitedGrid[nRow][nCol] = color
                    q.append((nRow, nCol))

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        visitedGrid = []
        for row in range(rows):
            tempArr = []
            for col in range(cols):
                tempArr.append(image[row][col])
            visitedGrid.append(tempArr)
        
        if image[sr][sc] == color:
            return image

        self.bfs(sr, sc, color, image, visitedGrid)
        return visitedGrid  