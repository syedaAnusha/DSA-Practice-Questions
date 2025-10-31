class Solution:
    # Optimal Approach
    # Time Complexity: O(log n*m)
    # Space Complexity: O(1)
    def findTarget(self, matrix, target):
        n = len(matrix);
        m = len(matrix[0]);
        low = 0;
        high = (n*m) - 1;

        while low <= high:
            mid = (low + high) // 2;
            row = mid // m;
            col = mid % m;

            if matrix[row][col] == target:
                return True;
            elif matrix[row][col] < target:
                low = mid + 1;
            else:
                high = mid - 1;
        return False;

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.findTarget(matrix, target);
        