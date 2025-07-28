class Solution(object):
    # Optimal Approach using hashing
    def findNQueens(self, col, board, ans, n, left, upperDiagonal, lowerDiagonal):
        if col == n:
            ans.append([''.join(row) for row in board]);
            return;
        else:
            for row in range(0, n):
                if left[row] == 0 and upperDiagonal[n-1 + col-row] == 0 and lowerDiagonal[row + col] == 0:
                    board[row][col]= 'Q';
                    left[row] = 1;
                    upperDiagonal[n-1 + col - row] = 1;
                    lowerDiagonal[row + col] = 1;
                    self.findNQueens(col+1, board, ans, n, left, upperDiagonal, lowerDiagonal);
                    board[row][col] = '.';
                    left[row] = 0;
                    lowerDiagonal[row + col] = 0;
                    upperDiagonal[n-1 + col - row] = 0;
                    
        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = [];
        col = 0;
        board = [['.' for _ in range(n)] for _ in range(n)];
        left = [0 for _ in range(n)];
        upperDiagonal = [0 for _ in range(2*n)];
        lowerDiagonal = [0 for _ in range(2*n)];
        self.findNQueens(col, board, ans, n, left, upperDiagonal, lowerDiagonal);
    
        return ans;
