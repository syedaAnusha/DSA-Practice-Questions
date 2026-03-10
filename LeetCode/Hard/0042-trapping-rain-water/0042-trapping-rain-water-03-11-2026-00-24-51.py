class Solution:
    # Better Approach
    # Time Complexity: O(n) + O(n)
    # Space Complexity: O(2n)
    def findNextAndPrevGreaterElem(self, arr):
        leftMax = -1;
        rightMax = -1;
        pge = [];
        nge = [];
        l = 0;
        r = len(arr)-1;
        while l < len(arr) and r >= 0:
            if arr[l] < leftMax:
                pge.append(leftMax);
            else:
                leftMax = arr[l];
                pge.append(0);
            if arr[r] < rightMax:
                nge.append(rightMax);
            else:
                rightMax = arr[r];
                nge.append(0);
            l += 1;
            r -= 1;
        return [pge, nge[::-1]];

    def trap(self, height: List[int]) -> int:
        totalUnitsOfWaterTrapped = 0;
        tple = self.findNextAndPrevGreaterElem(height);
        pge = tple[0];
        nge = tple[1];
        for i in range(len(height)):
            if pge[i] > height[i] and height[i] < nge[i]:
                totalUnitsOfWaterTrapped += min(pge[i], nge[i]) - height[i];
        return totalUnitsOfWaterTrapped;       