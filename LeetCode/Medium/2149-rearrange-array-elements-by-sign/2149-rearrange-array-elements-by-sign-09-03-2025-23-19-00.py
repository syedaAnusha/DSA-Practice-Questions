class Solution(object):
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(nums);
        positiveIndex = 0;
        negativeIndex = 1;
        for i in range(len(nums)):
            if nums[i] < 0:
                ans[negativeIndex] = nums[i];
                negativeIndex += 2;
            else:
                ans[positiveIndex] = nums[i];
                positiveIndex += 2;     
        return ans;