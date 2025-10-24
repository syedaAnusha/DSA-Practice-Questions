class Solution:
    # Brute Force Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums);
        for i in range(n):
            if (i == 0 or nums[i] > nums[i-1]) and (i == n-1 or nums[i] > nums[i+1]):
                return i;
           

        