class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def trap(self, height: List[int]) -> int:
        totalUnitsOfWaterTrapped = 0;
        leftMax = rightMax = 0;
        left = 0;
        right = len(height)-1;

        while left < right:
            if height[left] <= height[right]:
                if leftMax > height[left]:
                    totalUnitsOfWaterTrapped += leftMax - height[left];
                else:
                    leftMax = height[left];
                left += 1;

            else:
                if rightMax > height[right]:
                    totalUnitsOfWaterTrapped += rightMax - height[right];
                else:
                    rightMax = height[right];
                right -= 1;
                
        return totalUnitsOfWaterTrapped;       