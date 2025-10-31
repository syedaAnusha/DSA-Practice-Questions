class Solution:
    # Brute Force Approach
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix);
        for i in range(row):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True;
        return False;
        