class Solution(object):
    # Better Approach
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashSet = {};
        for i in range(len(nums)):
            numToFind = target - nums[i];
            if numToFind in hashSet:
                j = hashSet[numToFind];
                return [i, j];
            hashSet[nums[i]] = i;


        