class Solution:
    # Brute Force Approach
    # Time Complexity: O(4n) + O(n)
    # Space Complexity: O(2n) + O(2n)
    def arrOfPrevSmallestElement(self, arr):
        stack = [];
        pse = [];
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop();
            if not stack:
                pse.append(-1);
            else:
                pse.append(stack[-1]);
            stack.append(i);
        return pse;
    
    def arrOfNextSmallestElement(self, arr):
        stack = [];
        nse = [];
        N = len(arr);
        for i in range(N-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop();
            if not stack:
                nse.append(N);
            else:
                nse.append(stack[-1]);
            stack.append(i);
        return nse[::-1];
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        nse = self.arrOfNextSmallestElement(heights);
        pse = self.arrOfPrevSmallestElement(heights);
        maxHeight = 0;
        for i in range(len(heights)):
            width = nse[i]-pse[i]-1;
            area = heights[i] * width;
            maxHeight = max(maxHeight, area);
        return maxHeight; 