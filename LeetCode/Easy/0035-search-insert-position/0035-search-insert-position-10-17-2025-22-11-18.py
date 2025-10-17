class Solution:
    # Optimal Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums);
        low = 0;
        high = n - 1;
        ind = n;

        while low <= high:
            mid = (low + high) // 2;
            if nums[mid] == target:
                return mid;
            elif nums[mid] > target:
                ind = mid;
                high = mid - 1;
            else:
                low = mid + 1;
        
        return ind;

        