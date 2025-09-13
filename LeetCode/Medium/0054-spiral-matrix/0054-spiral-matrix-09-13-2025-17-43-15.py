class Solution(object):
    # Optimal Approach
    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top = 0;
        left = 0;
        right = len(matrix[0])-1;
        bottom = len(matrix)-1;
        spiralMatrix = [];

        while left <= right and top <= bottom:
            # Move left to right
            for i in range(left, right+1):
                spiralMatrix.append(matrix[top][i]);
            top += 1;
        
            # move top to bottom
            for j in range(top, bottom+1):
                spiralMatrix.append(matrix[j][right]);
            right -= 1;

            # move right to left
            if top <= bottom:
                k = right;
                while k >= left:
                    spiralMatrix.append(matrix[bottom][k]);
                    k -= 1;
                bottom -= 1;

            # move bottom to top
            if left <= right:
                l = bottom;
                while l >= top:
                    spiralMatrix.append(matrix[l][left]);
                    l -= 1;
                left += 1;
        return spiralMatrix;

        

        