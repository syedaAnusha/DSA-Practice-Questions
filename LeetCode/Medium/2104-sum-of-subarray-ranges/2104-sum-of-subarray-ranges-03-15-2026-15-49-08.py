class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def subArrayRanges(self, nums: List[int]) -> int:
        SumOfRange = 0;
        for i in range(len(nums)):
            minVal = nums[i];
            maxVal = nums[i];
            for j in range(i, len(nums)):
                minVal = min(minVal, nums[j]);
                maxVal = max(maxVal, nums[j]);
                SumOfRange += (maxVal - minVal);
        return SumOfRange;        