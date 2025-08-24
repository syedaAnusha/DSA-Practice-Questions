class Solution(object):
    # Optimal Force Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # check if array is sorted and rotated
    def checkArray(self, nums):
        numsLen = len(nums)-1;
        rotationCounter = 0;
        for i in range(0, numsLen):
            if nums[i] > nums[i+1]:
                rotationCounter += 1;
        if nums[numsLen] > nums[0]:
            rotationCounter += 1;
        if rotationCounter >= 2:
            return False;
        return True;
    
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.checkArray(nums);
        