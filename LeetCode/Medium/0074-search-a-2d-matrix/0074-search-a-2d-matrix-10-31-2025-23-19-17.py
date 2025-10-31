class Solution:
    # Better Approach
    # Time Complexity: O(n) + O(log m)
    # Space Complexity: O(1)
    def findTarget(self, arr, target):
        n = len(arr);
        low = 0;
        high = n - 1;

        while low <= high:
            mid = (low + high) // 2;
            if arr[mid] == target:
                return True;
            elif arr[mid] < target:
                low = mid + 1;
            else:
                high = mid - 1;
        return False;

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix);
        for i in range(row):
            if matrix[i][0] <= target and target <= matrix[i][len(matrix[i])-1]:
                return self.findTarget(matrix[i], target);
        return False;
        