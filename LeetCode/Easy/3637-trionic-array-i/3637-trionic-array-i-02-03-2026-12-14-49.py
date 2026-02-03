class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isTrionic(self, nums: List[int]) -> bool:
        p = 0;
        q = 0;
        r = 0;
        i = 0;
        j = 1;

        while i < j and j < len(nums):
            if nums[i] < nums[j] and q == 0:
                p = j; # strictly increasing
            elif nums[i] > nums[j] and r == 0:
                q = j; # strictly decreasing
            elif nums[i] < nums[j]:
                r = j; # strictly increasing
            else:
                return False; # if violates the order
            i += 1;
            j += 1;
        if 0 < p and p < q and q < r:
            return True;
        return False;       