class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums);
        if nums[0] >= N:
            return True;
        maxReachedIndex = 0;
        i = 0;
        while i < N:
            if i > maxReachedIndex:
                return False;
            indexToReach = i + nums[i];
            maxReachedIndex = max(maxReachedIndex, indexToReach);
            i += 1;
        return True;

