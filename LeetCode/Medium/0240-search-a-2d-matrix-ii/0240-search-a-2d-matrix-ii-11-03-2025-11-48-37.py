class Solution:
    # Optimal Approach
    # Time Complexity: O(n + m)
    # Space Complexity: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix);
        numCols = len(matrix[0]);
        curRow, curCol = 0, numCols - 1;

        # handling edge case
        if len(matrix) == 0:
            return False;

        while curRow < numRows and curCol >= 0:
            if matrix[curRow][curCol] == target:
                return True;
            elif matrix[curRow][curCol] < target:
                curRow += 1;
            else:
                curCol -= 1;
        return False;


        