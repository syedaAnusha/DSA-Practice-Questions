class Solution(object):
    def findSudoku(self, k, listOfemptyCells, board, rows, cols, subgrid):
        if k == len(listOfemptyCells):
            return True;

        i, j = listOfemptyCells[k];
        for char in '123456789':
            if char not in rows[i] and char not in cols[j] and char not in subgrid[3*(i // 3) + j // 3]:
                board[i][j] = char;

                rows[i].add(char);
                cols[j].add(char);
                subgrid[3*(i // 3) + j // 3].add(char);

                if self.findSudoku(k+1, listOfemptyCells, board, rows, cols, subgrid):
                    return True;
                
                board[i][j] = '.';

                rows[i].remove(char);
                cols[j].remove(char);
                subgrid[3*(i // 3) + j // 3].remove(char);
        return False;
                     

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)];
        cols = [set() for _ in range(9)];
        subgrid = [set() for _ in range(9)];
        listOfemptyCells = [];

        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == '.':
                    listOfemptyCells.append((row, col));
                else:
                    value = board[row][col];
                    rows[row].add(value);
                    cols[col].add(value);
                    subgrid[3*(row//3) + col // 3].add(value);

        self.findSudoku(0, listOfemptyCells, board, rows, cols, subgrid);
        