class Solution(object):
    # Brute Force / Better Approach
    # Time Complexity: O(n)*O(n) = near about O(n^2) since j = i
    # Space Complexity: O(1)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = float('-inf');
        for i in range(len(nums)):
            Sum = 0;
            for j in range(i, len(nums)):
                Sum += nums[j];
                maxSum = max(maxSum, Sum);
        return maxSum;
