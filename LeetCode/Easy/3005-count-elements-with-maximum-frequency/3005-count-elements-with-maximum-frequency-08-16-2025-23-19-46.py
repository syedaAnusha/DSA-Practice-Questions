class Solution(object):
    def getHashTable(self, nums):
        # method 1
        hashTable = {};
        maxCount = 1;
        for i in range(len(nums)):
            if nums[i] in hashTable:
                hashTable[nums[i]] += 1;
            else:
                hashTable[nums[i]] = 1;
            maxCount = max(maxCount, hashTable[nums[i]]);
        
        tple = (hashTable, maxCount);
        return tple;

    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tple = self.getHashTable(nums);
        table = tple[0];
        maxFrequency = tple[1];
    
        numFrequency = 0;
        for value in table.values():
            if value == maxFrequency:
                numFrequency += 1;

        res = maxFrequency * numFrequency; 
        return res; 

        
        