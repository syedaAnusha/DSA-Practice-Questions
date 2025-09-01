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
        ansStart = -1;
        ansEnd = -1;
        startIndex = -1;
        for i in range(len(nums)):
            if Sum == 0:
                startIndex = i;

            Sum += nums[i];
            if Sum < 0:
                maxSum = max(maxSum, Sum);
                Sum = 0;
                ansIndex = startIndex;
                ansEnd = i
            else:
                if Sum > maxSum:
                    maxSum = max(maxSum, Sum);
                    ansStart = startIndex;
                    ansEnd = i

        print('Subarray:',nums[ansStart:ansEnd+1]);
        return maxSum;

                

