class Solution:
    # Brute Force Approach
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxCnt = -1;
        index = -1;
        for i in range(len(mat)):
            cntRow = 0;
            for j in range(len(mat[i])):
                cntRow += mat[i][j];
            if cntRow > maxCnt:
                maxCnt = cntRow;
                index = i;
        return [index, maxCnt];
        