class Solution:
    # Optimal Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findMin(self, nums: List[int]) -> int:
        n = len(nums);
        low = 0;
        high = n - 1;
        minValue = float('inf');

        while low <= high:
            mid = (low + high) // 2;
            if nums[low] <= nums[high]:
                return min(minValue,nums[low]);

            if nums[low] <= nums[mid]:
                minValue = min(minValue, nums[low]);
                low = mid + 1;
            else:
                minValue = min(minValue, nums[mid]);
                high = mid - 1;

        return minValue;


        