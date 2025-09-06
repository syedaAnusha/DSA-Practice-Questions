class Solution(object):
    # Brute Force Approach
    # Time Complexity: [O(nxm) * O(n+m)] + O(n*m) = O(n^3)
    # Space Complexity: O(1)
    def markRow(self, matrix, row):
        for col in range(len(matrix[0])):
            if matrix[row][col] != 0:
                matrix[row][col] = float('-inf');

    def markCol(self, matrix, col):
        for row in range(len(matrix)):
            if matrix[row][col] != 0:
                matrix[row][col] = float('-inf');

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    self.markRow(matrix, row);
                    self.markCol(matrix, col);

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == float('-inf'):
                    matrix[row][col] = 0;

        