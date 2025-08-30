class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subarrayCnt = 0;
        for i in range(len(nums)):
            Sum = 0;
            for j in range(i, len(nums)):
                Sum += nums[j];
                if Sum == k:
                    subarrayCnt += 1;
        return subarrayCnt;
