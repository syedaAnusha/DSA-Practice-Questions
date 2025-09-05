class Solution(object):
    # Optimal Approach
    # Time Complexity: O(n) + O(n) + O(n) = O(3n) = O(n)
    # Space Complexity: O(1) -> in-place, 
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i];
    
    def reverseArr(self, nums, index):
        i = index;
        j = len(nums)-1;
        while i <= j:
            self.swap(nums, i, j);
            i += 1;
            j -= 1;

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = -1;
        i = len(nums)-2;
        while i >= 0:
            if nums[i] < nums[i+1]:
                index = i;
                break;
            i -= 1;

        # edge case: if there is no dip e.g [5,4,3,2,1]
        if index == -1:
            nums.reverse();
            return;

        j = len(nums)-1;
        while j > index:
            if nums[j] > nums[index]:
                self.swap(nums, j, index);
                break;
            j -= 1;

        self.reverseArr(nums, index+1);
        


        
        

        