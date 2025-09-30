class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = float('-inf');
        for i in range(len(nums)):
            product = nums[i];
            maxProduct = max(maxProduct, product);
            for j in range(i+1, len(nums)):
                product *= nums[j];
                maxProduct = max(maxProduct, product);  
        return maxProduct;
