class Solution:
    # Optimal Approach - 01
    # Time Complexity: 2 * O(log n)
    # Space Complexity: O(1)
    def findLowerBound(self, nums, target):
        n = len(nums);
        low = 0
        high = n - 1;
        firstIndex = n;
        while low <= high:
            mid = (low + high) // 2;
            if nums[mid] >= target:
                firstIndex = mid;
                high = mid - 1;
            else:
                low = mid + 1;
        return firstIndex;
    
    def findUpperBound(self, nums, target):
        n = len(nums);
        low = 0;
        high = n - 1;
        lastIndex = n;
        while low <= high:
            mid = (low + high) // 2;
            if nums[mid] > target:
                lastIndex = mid;
                high = mid - 1;
            else:
                low = mid + 1;
        return lastIndex;


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums);
        firstIndex = self.findLowerBound(nums, target);
        lastIndex = self.findUpperBound(nums, target);

        if n == 0 or firstIndex == n or nums[firstIndex] != target:
            return [-1, -1];
        else:
            return [firstIndex, lastIndex-1];
        