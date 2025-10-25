class Solution:
    # Brute Force Approach
    # Time Complexity: O(nlogn) + O(n)
    # Space Complexity: O(n)
    def maximumGap(self, nums: List[int]) -> int:
        sortedNums = nums.sort();
        maxDifference = 0;
        n = len(nums);
        if n < 2:
            return maxDifference;
        for i in range(n-1):
            currentDiff = nums[i+1] - nums[i];
            maxDifference = max(maxDifference, currentDiff);
        return maxDifference;
        