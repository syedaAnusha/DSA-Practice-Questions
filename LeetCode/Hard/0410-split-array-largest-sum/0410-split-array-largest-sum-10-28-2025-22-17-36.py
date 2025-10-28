class Solution:
    # Optimal Approach
    # Time Complexity: O(log (sum - max + 1)) * O(n)
    # Space Complexity: O(1)
    def getSubarrays(self, nums, maxSum):
        totalSubarrays = 1;
        Sum = 0;
        for i in range(len(nums)):
            if nums[i] + Sum <= maxSum:
                Sum += nums[i];
            else:
                totalSubarrays += 1;
                Sum = nums[i];
        return totalSubarrays;

    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums);
        high = sum(nums);

        if len(nums) < k:
            return -1;

        while low <= high:
            mid = (low + high) // 2;
            if self.getSubarrays(nums, mid) <= k:
                high = mid - 1;
            else:
                low = mid + 1;
        return low;
        