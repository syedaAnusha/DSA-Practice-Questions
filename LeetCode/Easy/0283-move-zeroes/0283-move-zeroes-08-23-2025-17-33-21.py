class Solution(object):
    # Brute Force Approch
    # Time Complexity: O(N) + O(T) + O(N) - O(T) = O(2N)
    # Space Complexity: O(T) or O(N): in worst-case
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = [];
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i]);

        for j in range(len(temp)):
            nums[j] = temp[j];
        
        for k in range(len(temp), len(nums)):
            nums[k] = 0;

        