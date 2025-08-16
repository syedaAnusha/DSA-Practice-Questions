class Solution(object):
    def findElementsOccurrenciesCount(self, nums):
        # method 2
        hashTable = {};
        maxFrequency = 0;
        numOfOccurrences = 0;
        for i in range(len(nums)):
            if nums[i] in hashTable:
                hashTable[nums[i]] += 1;
            else:
                hashTable[nums[i]] = 1;
            maxFrequency = max(maxFrequency, hashTable[nums[i]]);
        
        if maxFrequency == 1:
            return len(nums);
        else:
            for value in hashTable.values():
                if value == maxFrequency:
                    numOfOccurrences += 1;
            return numOfOccurrences * maxFrequency;

    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.findElementsOccurrenciesCount(nums);

        
        