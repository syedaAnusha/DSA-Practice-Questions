from collections import deque
class Solution:
    # Optimal Approach
    # Time Complexity: O(n*m) + O(n*m*4)
    # Space Complexity: O(n*m)
    def dfs(self, row, col, board, visitedBoard):
        visitedBoard[row][col] = 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nRow = row + dr
            nCol = col + dc
            if (nRow >= 0 and nRow < len(board) and 
                nCol >= 0 and nCol < len(board[0]) and 
                board[nRow][nCol] == 'O' 
                and visitedBoard[nRow][nCol] == 0):
                    self.dfs(nRow, nCol, board, visitedBoard)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visitedBoard = [[0]*cols for _ in range(rows)]

        # traverse first and last row
        for col in range(cols):
            # first row
            if board[0][col] == 'O' and visitedBoard[0][col] == 0:
                self.dfs(0, col, board, visitedBoard)
            
            # last row
            if board[rows-1][col] == 'O' and visitedBoard[rows-1][col] == 0:
                self.dfs(rows-1, col, board, visitedBoard)
        
        # traverse first and last col
        for row in range(rows):
            # first col
            if board[row][0] == 'O' and visitedBoard[row][0] == 0:
                self.dfs(row, 0, board, visitedBoard)
            
            # last col
            if board[row][cols-1] == 'O' and visitedBoard[row][cols-1] == 0:
                self.dfs(row, cols-1, board, visitedBoard)
        
        for row in range(rows):
            for col in range(cols):
                if visitedBoard[row][col] == 0 and board[row][col] == 'O':
                    board[row][col] = 'X'   