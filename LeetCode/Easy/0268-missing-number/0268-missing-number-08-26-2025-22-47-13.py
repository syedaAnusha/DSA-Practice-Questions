class Solution(object):
    # Brute Force Approch 2
    # Time Complexity: O(n) + O(n) = O(2n) = O(n)
    # Space Complexity : O(n)
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums);
        for i in range(len(nums)+1):
            if i not in numsSet:
                return i;
        