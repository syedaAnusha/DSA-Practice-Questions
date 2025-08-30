class Solution(object):
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n/2 + 1)
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashTable = {0:1};
        prefixSum = 0;
        subarrayCounter = 0;
        for i in range(len(nums)):
            prefixSum += nums[i];
            rem = prefixSum - k;
            if rem in hashTable:
                subarrayCounter += hashTable[rem];
            if prefixSum not in hashTable:
                hashTable[prefixSum] = 1;
            else:
                hashTable[prefixSum] += 1;

        return subarrayCounter;