class Solution(object):
    # Optimal Approch
    # Time Complexity: O(n)
    # Space Complexity : O(1)
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums);
        missingNum = n*(n+1) // 2;
        for i in range(len(nums)):
            if nums[i] != 0:
                missingNum -= nums[i];

        return missingNum;
        