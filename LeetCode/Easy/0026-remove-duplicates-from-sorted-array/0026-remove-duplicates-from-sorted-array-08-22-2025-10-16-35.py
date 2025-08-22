class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # OPTIMAL APPROACH - Using 2 pointers
        # Time Complexity: O(n)
        # Space Complexity: O(1);
        i = 0;
        j = 1;
        while i < len(nums) and j < len(nums):
            if nums[j] != nums[i]:
                i = i+1;
                nums[i] = nums[j];
            j += 1;
        return i+1;






        