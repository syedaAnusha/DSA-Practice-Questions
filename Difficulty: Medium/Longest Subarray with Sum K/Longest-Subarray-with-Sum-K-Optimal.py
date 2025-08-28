class Solution(object):
		# Optimal Solution - Using Two pointers for arrays contain only [0, positives]
		# Time Complexity: O(2n) = O(n)
		# Space Complexity: O(1)
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0;
        right = 0;
        Sum = 0;
        maxLen = 0;
        while left <= right and right < len(nums):
            Sum += nums[right];
            if Sum == k:
                maxLen = max(maxLen, right-left+1);
            if Sum > k:
                Sum -= nums[left];
                left += 1;
            if Sum <= k:
                right += 1;
        return maxLen;
