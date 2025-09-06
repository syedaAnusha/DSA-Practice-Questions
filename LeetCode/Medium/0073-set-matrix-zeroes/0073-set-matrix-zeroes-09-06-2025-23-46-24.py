class Solution(object):
    # Optimal Approach
    # Time Complexity: O(n*m) + O(n*m) = O(2*n*m)
    # Space Complexity: O(1) // or just using for 1 variable which is col0
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # rows --> matrix[0][n]
        # cols --> matrix[m][0]
        col0 = 1;
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    # mark the i-th row
                    matrix[row][0] = 0;  
                    if col != 0:
                        # mark the j-th col
                        matrix[0][col] = 0;
                    else:
                        col0 = 0;
                    
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0;

        if matrix[0][0] == 0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0;

        if col0 == 0:
            for row in range(len(matrix)):
                matrix[row][0] = 0;



                    
                