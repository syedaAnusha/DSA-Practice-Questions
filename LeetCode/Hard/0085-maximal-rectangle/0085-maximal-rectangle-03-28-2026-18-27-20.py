class Solution:
    # Optimal Approach
    # Time Complexity: O(n * (m + 2n))
    # Space Complexity: O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [];
        maxArea = 0;
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                curBar = stack.pop();
                nse = i;
                if not stack:
                    pse = -1;
                else:
                    pse = stack[-1];
                width = nse - pse - 1;
                curArea = heights[curBar] * width;
                maxArea = max(maxArea, curArea);
            stack.append(i);
        
        while stack:
            curBar = stack.pop();
            nse = len(heights);
            if not stack:
                pse = -1;
            else:
                pse = stack[-1];
            width = nse - pse - 1;
            curArea = heights[curBar] * width;
            maxArea = max(maxArea, curArea);
         
        return maxArea; 

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix);
        cols = len(matrix[0]);
        heights = [0]*cols;
        maxArea = 0;
        for row in range(rows):
            for col in range(cols):
                if int(matrix[row][col]) == 0:
                    heights[col] = 0;
                else:
                    heights[col] += 1;
            maxArea = max(maxArea, self.largestRectangleArea(heights));
        return maxArea;