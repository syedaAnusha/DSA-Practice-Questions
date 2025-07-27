class Solution(object):
    def findNQueens(self, n, col, leftRow, upperDiagonal, lowerDiagonal, ans, board):
        if col == n:
            ans.append(list(board));
            return;
        else:
            for row in range(0, n):
                if leftRow[row] == 0 and upperDiagonal[n-1 + col-row] == 0 and lowerDiagonal[row+col] == 0:
                    curr_row = list(board[row]);
                    curr_row[col] = 'Q';
                    board[row] = "".join(curr_row);
                    leftRow[row] = 1;
                    upperDiagonal[n-1 + col-row] = 1;
                    lowerDiagonal[row+col] = 1;
                    self.findNQueens(n, col+1, leftRow, upperDiagonal, lowerDiagonal, ans, board);
                    curr_row = list(board[row]);
                    curr_row[col] = '.';
                    board[row] = "".join(curr_row);
                    leftRow[row] = 0;
                    upperDiagonal[n-1 + col-row] = 0;
                    lowerDiagonal[row+col] = 0; 

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [n*'.' for _ in range(n)];
        leftRow = [0 for _ in range(n)];
        upperDiagonal = [0 for _ in range(2*n)];
        lowerDiagonal = [0 for _ in range(2*n)];
        ans = [];
        self.findNQueens(n, 0, leftRow, upperDiagonal, lowerDiagonal, ans, board);
        totalBoards = len(ans);
        return totalBoards;
        