class Solution(object):
    # Optimal Approach - Using Kandane's Algorithm
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = float('-inf');
        Sum = 0;
        for i in range(len(nums)):
            Sum += nums[i];
            if Sum < 0:
                maxSum = max(maxSum, Sum);
                Sum = 0;
            else:
                maxSum = max(maxSum, Sum);
        return maxSum;

                

