class Solution(object):
    # Brute Force Approch
    # Time Complexity: O(n)^2
    # Space Complexity : O(1)
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)+1):
            if i not in nums:
                return i;
        
