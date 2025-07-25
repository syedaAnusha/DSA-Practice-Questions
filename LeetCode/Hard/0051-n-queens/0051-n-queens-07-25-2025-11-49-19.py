class Solution(object):
    # Brute Force Approach
    def isSafe(self, row, col, n, board):
        duprow = row;
        dupcol = col;

        # check for all QUEENS in left upper diagonals
        while(row >= 0 and col >= 0):
            if board[row][col] == 'Q':
                return False;
            row -= 1;
            col -= 1;
        
        row = duprow;
        col = dupcol;
        # check for all QUEENS in left
        while(col >= 0):
            if board[row][col] == 'Q':
                return False;
            col -= 1;

        row = duprow;
        col = dupcol;
        # check for all QUEENS in left below diagonal
        while(row < n and col >= 0):
            if board[row][col] == 'Q':
                return False;
            row += 1;
            col -= 1;
        
        return True;

    def findNQueens(self, col, board, ans, n):
        if col == n:
            ans.append(list(board));
            return;
        else:
            for i in range(0, n):
                if self.isSafe(i, col, n, board):
                    cur_row = list(board[i]); # Convert string to a list of characters for modification
                    cur_row[col] = 'Q';
                    board[i] = "".join(cur_row); # Join the list of characters back into a string
                    self.findNQueens(col+1, board, ans, n);
                    cur_row = list(board[i]);
                    cur_row[col] = '.';
                    board[i] = "".join(cur_row);
        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = [];
        col = 0;
        board = [n*'.' for _ in range(n)];
        self.findNQueens(col, board, ans, n);
        return ans;
