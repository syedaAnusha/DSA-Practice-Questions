class Solution:
    # Optimal Approach
    # Time Complexity: O(n * log m)
    # Space Complexity: O(1)
    def findMaxElem(self, mat, mid):
        numRows = len(mat);
        maxElem = -1;
        index = -1;
        for row in range(numRows):
            if mat[row][mid] > maxElem:
                maxElem = mat[row][mid];
                index = row;
        return index;

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        numRows = len(mat);
        numCols = len(mat[0]);

        low = 0;
        high = numCols - 1;

        while low <= high:
            mid = (low + high) // 2;
            row = self.findMaxElem(mat, mid);
            if mid-1 >= 0:
                left = mat[row][mid-1];
            else:
                left = -1;
            if mid + 1 < numCols:
                right = mat[row][mid+1];
            else:
                right = -1;
            
            if left < mat[row][mid] and mat[row][mid] > right:
                return [row, mid];
            elif mat[row][mid] < left:
                high = mid - 1;
            else:
                low = mid + 1;