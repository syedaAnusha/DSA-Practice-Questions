class Solution:
    # Brute Force Approach
    # Time Complexity: O(4*m*n)
    # Space Complexity: O(1)
    def checkLargestElem(self, mat, row, col):
        lstRow = len(mat)-1;
        lstCol = len(mat[row])-1

        top = mat[row - (row != 0)][col];
        left = mat[row][col - (col != 0)];
        bottom = mat[row + (row != lstRow)][col];
        right = mat[row][col + (col != lstCol)];

        largestVal = mat[row][col];
        if top == largestVal:
            top = -1;
        if left == largestVal:
            left = -1;
        if largestVal == bottom:
            bottom = -1;
        if largestVal == right:
            right = -1;

        if largestVal > top and largestVal > left and largestVal > bottom and largestVal > right:
            return True;
        else:
            return False;
   

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        numRows = len(mat);
        numCols = len(mat[0]);
        arr = []
        for row in range(numRows):
            for col in range(numCols):
                if self.checkLargestElem(mat, row, col):
                    arr = [row, col];
        return arr;