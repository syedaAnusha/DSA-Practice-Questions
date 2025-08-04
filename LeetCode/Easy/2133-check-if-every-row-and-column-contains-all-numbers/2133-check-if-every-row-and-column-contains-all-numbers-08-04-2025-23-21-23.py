class Solution(object):
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
                rows[row].add(value);
                cols[col].add(value);

        while index < matrix_size:
            if rows[index] == cols[index] and len(rows[index]) == matrix_size and len(cols[index]) == matrix_size:
                index += 1;
                continue;
            return False;
        return True;
        

        