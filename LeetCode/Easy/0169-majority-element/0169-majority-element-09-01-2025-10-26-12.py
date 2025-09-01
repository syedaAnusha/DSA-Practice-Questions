class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(n) * O(n) = O(n^2)
    # Space Complexity: O(1)
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            cnt = 0;
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    cnt += 1;
            
            if cnt > (len(nums) // 2):
                return nums[i];
