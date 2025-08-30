class Solution(object):
    # Better Approach
    # Time Complexity = O(n) + O(n) = O(2n) = O(n) 
    # Space Complexity = O(1)
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt0 = 0;
        cnt1 = 0;
        cnt2 = 0;
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt0 += 1;
            elif nums[i] == 1:
                cnt1 += 1;
            else:
                cnt2 += 1;

        j = 0;
        cnt0Len =  cnt0;
        cnt1Len = cnt1;
        cnt2Len = cnt2;

        while cnt0 > 0:
            nums[j] = 0;
            cnt0 -= 1;
            j += 1;
        
        while cnt1 > 0:
            nums[j] = 1;
            cnt1 -= 1;
            j += 1;
        
        while cnt2 > 0:
            nums[j] = 2;
            cnt2 -= 1;
            j += 1;
        
        