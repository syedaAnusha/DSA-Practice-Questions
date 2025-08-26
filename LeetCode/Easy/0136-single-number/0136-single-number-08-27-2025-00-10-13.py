class Solution(object):
    # Optimal Approach:
    # Time Compplexity: O(n)
    # Space Complexity: O(1)
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        singleNum = 0;
        for i in range(len(nums)):
            singleNum = singleNum ^ nums[i];
        return singleNum;

