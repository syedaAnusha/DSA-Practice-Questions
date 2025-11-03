class Solution:
    # Better Approach
    # Time Complexity: O(n * log m)
    # Space Complexity: O(1)
    def findTarget(self, rowMat, target):
        low = 0;
        high = len(rowMat)-1;
        while low <= high:
            mid = (low + high) // 2;
            if rowMat[mid] == target:
                return True;
            elif rowMat[mid] < target:
                low = mid + 1;
            else:
                high = mid - 1;
        return False;

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix);
        cols = len(matrix[0]);
        for i in range(rows):
            if self.findTarget(matrix[i], target):
                return True;
        return False;



        