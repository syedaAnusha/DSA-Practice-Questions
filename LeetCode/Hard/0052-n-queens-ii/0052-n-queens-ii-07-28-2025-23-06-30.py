class Solution(object):
    def findNQueens(self, n, col, leftRow, upperDiagonal, lowerDiagonal, board):
        # Approach 2
        if col == n:
            return 1;
        else:
            totalQueens = 0;
            for row in range(0, n):
                if leftRow[row] == 0 and upperDiagonal[n-1 + col-row] == 0 and lowerDiagonal[row+col] == 0:
                    board[row][col] = 'Q';
                    leftRow[row] = 1;
                    upperDiagonal[n-1 + col-row] = 1;
                    lowerDiagonal[row+col] = 1;
                    totalQueens += self.findNQueens(n, col+1, leftRow, upperDiagonal, lowerDiagonal,board);
                    board[row][col] = ".";
                    leftRow[row] = 0;
                    upperDiagonal[n-1 + col-row] = 0;
                    lowerDiagonal[row+col] = 0;
        return totalQueens;
                


    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [['.' for _ in range(n)] for _ in range(n)];
        leftRow = [0 for _ in range(n)];
        upperDiagonal = [0 for _ in range(2*n)];
        lowerDiagonal = [0 for _ in range(2*n)];

        return self.findNQueens(n, 0, leftRow, upperDiagonal, lowerDiagonal,board);
        