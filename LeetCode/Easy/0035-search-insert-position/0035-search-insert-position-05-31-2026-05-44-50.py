class Solution:
    # Optimal Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        numsLength = len(nums);
        low = 0;
        high = numsLength - 1;
        while low <= high:
            mid = (low + high) // 2;
            if nums[mid] < target:
                low = mid + 1;
            elif nums[mid] > target:
                high = mid - 1;
            else:
                return mid;
        return high + 1;
        
        

        