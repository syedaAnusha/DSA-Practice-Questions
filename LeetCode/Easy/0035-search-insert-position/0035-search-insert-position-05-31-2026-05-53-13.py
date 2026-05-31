class Solution:
    # Optimal Approach
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchInsert(self, nums: List[int], target: int) -> int:
        numsLength = len(nums);
        low = 0;
        high = numsLength - 1;
        index = numsLength;
        
        while low <= high:
            mid = (low + high) // 2;
            if nums[mid] >= target:
                index = mid;
                high = mid - 1;
            else:
                low = mid + 1;
        return index;
        
        

        