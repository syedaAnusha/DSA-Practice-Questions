class Solution(object):
    # Better Approach
    # Time Complexity: O(n*m) + O(n*m) = O(2*n*m)
    # Space Complexity: O(n) + O(m)
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = [0]*len(matrix);
        cols = [0]*len(matrix[0]);
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows[row] = 1;
                    cols[col] = 1;

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if rows[row] == 1 or cols[col] == 1:
                    matrix[row][col] = 0;