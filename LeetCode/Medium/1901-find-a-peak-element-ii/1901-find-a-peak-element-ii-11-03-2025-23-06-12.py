class Solution:
    # Optimal Approach
    # Time Complexity: O(n * log m)
    # Space Complexity: O(1)
    # Finding Peak Element using rows
    def findMaxElemIndex(self, mat, mid):
        numCols = len(mat[0]);
        maxElem = -1;
        index = -1;
        for col in range(numCols):
            if mat[mid][col] > maxElem:
                maxElem = mat[mid][col];
                index = col;
        return index;

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        numRows = len(mat);
        low = 0;
        high = numRows-1;

        while low <= high:
            mid = (low + high) // 2;
            maxColIndex = self.findMaxElemIndex(mat, mid);
            top = mat[mid-1][maxColIndex] if mid-1 >= 0 else -1;
            bottom = mat[mid+1][maxColIndex] if mid+1 < numRows else -1;
            if top < mat[mid][maxColIndex] and mat[mid][maxColIndex] > bottom:
                return [mid, maxColIndex];
            elif top > mat[mid][maxColIndex]:
                high = mid - 1;
            else:
                low = mid + 1;