class Solution(object):
    # Approach - 2
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        matrix_size = len(matrix[0]);
        rows = [set() for _ in range(matrix_size)];
        cols = [set() for _ in range(matrix_size)];
        index = 0;
        for row in range(0, matrix_size):
            for col in range(0, matrix_size):
                value = matrix[row][col];
                if value not in rows[row] and value not in cols[col]:
                    rows[row].add(value);
                    cols[col].add(value);
                else:
                    return False;
        return True;
        

        