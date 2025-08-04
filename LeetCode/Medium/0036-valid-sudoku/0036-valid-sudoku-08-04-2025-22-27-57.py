import pprint
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)];
        cols = [set() for _ in range(9)];
        subgrid = [set() for _ in range(9)];
        
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    value = board[i][j];
                    if value not in rows[i] and value not in cols[j] and value not in subgrid[3*(i//3) + j//3]:
                        rows[i].add(value);
                        cols[j].add(value);
                        subgrid[3*(i//3) + j//3].add(value);
                    else:
                        return False;

        return True;
        