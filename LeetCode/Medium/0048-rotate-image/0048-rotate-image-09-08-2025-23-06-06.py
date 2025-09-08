class Solution(object):
    # Optimal Approach
    # Time Complexity: O(n/2)*O(n/2) + O(n)*O(n/2)
    # Space Complexity: O(1)
    def swap(self, arr, row, col):
        arr[row][col], arr[col][row] = arr[col][row], arr[row][col];

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix);
        # Transpose matrix that is, convert rows to cols and cols to rows
        for row in range(n-1):
            for col in range(row+1, n):
                self.swap(matrix, row, col);

        # Reverse every row
        for row in range(n):
                matrix[row].reverse();
            