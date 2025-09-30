class Solution:
    # Optimal Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        lengthOfArray = len(nums);
        maxProduct = float('-inf');
        prefix = 1;
        suffix = 1;
        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1;
            if suffix == 0:
                suffix = 1;
            prefix *= nums[i];
            suffix *= nums[lengthOfArray-i-1];
            maxProduct = max(maxProduct, max(prefix, suffix));
        return maxProduct;