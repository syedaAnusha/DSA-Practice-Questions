class Solution(object):
    # Better Approach
    # Time Complexity: O(n) + O(n) = O(2n) = O(n)
    # Space Complexity: O(n)
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countFrequencySet = {};
        maxFreq = len(nums) // 2;
        for i in range(len(nums)):
            if nums[i] in countFrequencySet:
                countFrequencySet[nums[i]] += 1;
            else:
                countFrequencySet[nums[i]] = 1;
            maxFreq = max(maxFreq, countFrequencySet[nums[i]]);
        
        for key, freq in countFrequencySet.items():
            if freq == maxFreq:
                return key;
