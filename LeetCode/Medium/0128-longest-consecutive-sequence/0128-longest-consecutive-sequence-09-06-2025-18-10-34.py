class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(n) * O(n) = O(n^2)
    # Space Complexity: O(1)
    def findConsecutives(self, arr, num):
        for i in range(len(arr)):
            if arr[i] == num:
                return True;
        return False;

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0;
        for i in range(len(nums)):
            cnt = 1;
            x = nums[i];
            while self.findConsecutives(nums, x+1):
                x = x+1;
                cnt += 1;
            longest = max(longest, cnt);
        return longest;
