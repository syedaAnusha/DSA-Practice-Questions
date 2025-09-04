class Solution(object):
    # Brute Force Approach - 2
    # what if we have any number of positives and negatives in nums array.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = [];
        neg = [];
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i]);
            else:
                pos.append(nums[i]);
        
        if len(pos) > len(neg):
            for j in range(len(neg)):
                nums[2*j] = pos[j];
                nums[(2*j)+1] = neg[j];
                
            index = len(neg)*2;
            for k in range(len(neg), len(pos)):
                nums[index] = pos[k];
                index += 1;
        else:
            for j in range(len(pos)):
                nums[2*j] = pos[j];
                nums[(2*j)+1] = neg[j];
                
            index = len(pos)*2;
            for k in range(len(pos), len(neg)):
                nums[index] = neg[k];
                index += 1;    
        return nums;