class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0;
        for i in range(len(nums)):
            xor = xor ^ nums[i];
        return xor;
        