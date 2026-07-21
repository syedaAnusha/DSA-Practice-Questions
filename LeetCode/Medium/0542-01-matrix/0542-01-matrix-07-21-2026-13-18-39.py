from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(n*m) + O(n*m*4)
    # Space Complexity: O(n*m)
    def findAllCellsWithDistanceZero(self, matrix, visitedMatrix, que):
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    visitedMatrix[row][col] = 1
                    que.append((row, col, 0))


    def IsValidCell(self, row, col, matrix, visitedMatrix):
        rows = len(matrix)
        cols = len(matrix[0])
        return (row >= 0 and row < rows and
                col >= 0 and col < cols and 
                visitedMatrix[row][col] == 0 and
                matrix[row][col] == 1)

    def bfs(self, matrix, visitedMatrix, resultantMatrix):
        q = deque([])
        self.findAllCellsWithDistanceZero(matrix, visitedMatrix, q)
        while q:
            row, col, distance = q.popleft()
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dr, dc in directions:
                nRow = row + dr
                nCol = col + dc
                if self.IsValidCell(nRow, nCol, matrix, visitedMatrix):
                    visitedMatrix[nRow][nCol] = 1
                    q.append((nRow, nCol, distance+1))

            resultantMatrix[row][col] = distance       

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        visitedMatrix = [[0] * cols for _ in range(rows)]
        resultantMatrix = [[0] * cols for _ in range(rows)]
        self.bfs(mat, visitedMatrix, resultantMatrix)
        return resultantMatrix      