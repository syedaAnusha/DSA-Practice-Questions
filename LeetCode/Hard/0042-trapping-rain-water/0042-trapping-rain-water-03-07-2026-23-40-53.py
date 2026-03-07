class Solution:
    # Brute Force Approach
    # Time Complexity: O(n) + O(n/2) + O(n)
    # Space Complexity: O(n)
    def reverseElem(self, arr):
        i = 0;
        j = len(arr)-1;
        while i < j:
            arr[i] , arr[j] = arr[j], arr[i];
            i += 1;
            j -= 1;
        return arr;

    def findSuffixMax(self, arr):
        lenOfArr = len(arr);
        suffMax = [];
        suffMax.append(arr[lenOfArr-1]);
        for i in range(lenOfArr-2, -1, -1):
            suffMax.append(max(suffMax[-1], arr[i]));
        
        return self.reverseElem(suffMax);

    def trap(self, height: List[int]) -> int:
        totalUnitsOfWaterTrapped = 0;
        maxHeightFromLeft = height[0];
        suffixMaxArr = self.findSuffixMax(height);

        for i in range(len(height)):
            leftMax = max(maxHeightFromLeft, height[i]);
            maxHeightFromLeft = leftMax;
            rightMax = suffixMaxArr[i];
            if height[i] < leftMax and height[i] < rightMax:
                totalUnitsOfWaterTrapped += min(leftMax, rightMax) - height[i];
        return totalUnitsOfWaterTrapped



        