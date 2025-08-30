class Solution(object):
    # Better Approach
    # Time Complexity = O(n) + O(n) = O(2n) = O(n) 
    # Space Complexity = O(1)
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i];

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0;
        mid = 0;
        high = len(nums)-1;
        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums, mid, low);
                low += 1;
                mid += 1;
            elif nums[mid] == 1:
                mid += 1;
            else:
                self.swap(nums, mid, high);
                high -= 1;

        