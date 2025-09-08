class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(n*n) + O(n*n) = (2*n*n) = O(n*n)
    # Space Complexity: O(n*n)
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix);
        ans = [[0 for _ in range(n)] for _ in range(n)];
        for row in range(n):
            for col in range(n):
                ans[col][(n-1)-row] = matrix[row][col];

        for row in range(n):
            for col in range(n):
                matrix[row][col] = ans[row][col];
        
        