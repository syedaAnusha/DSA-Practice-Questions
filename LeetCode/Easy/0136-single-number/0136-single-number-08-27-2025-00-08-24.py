class Solution(object):
    # Brute Force Approach:
    # Time Compplexity: O(n) + O(n) = O(2n) = O(n);
    # Space Complexity: O(n)
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countSet = {};
        for i in range(len(nums)):
            if nums[i] in countSet:
                countSet[nums[i]] += 1;
            else:
                countSet[nums[i]] = 1;

        for key, value in countSet.items():
            if value == 1:
                return key;
