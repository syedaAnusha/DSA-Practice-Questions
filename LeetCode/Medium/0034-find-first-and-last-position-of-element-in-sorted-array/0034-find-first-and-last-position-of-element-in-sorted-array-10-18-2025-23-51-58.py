class Solution:
    # Optimal Approach - 02
    # Time Complexity: O(log n) + O(log n) = (2 O(log n))
    # Space Complexity: O(1)
    def findFirstOccurence(self, nums, target):
        n = len(nums);
        low = 0
        high = n - 1;
        firstIndex = -1;
        while low <= high:
            mid = (low + high) // 2;
            if nums[mid] == target:
                firstIndex = mid;
                high = mid - 1;
            elif nums[mid] < target:
                low = mid + 1;
            else:
                high = mid - 1;
        return firstIndex;
    
    def findSecondOccurence(self, nums, target):
        n = len(nums);
        low = 0;
        high = n - 1;
        lastIndex = -1;
        while low <= high:
            mid = (low + high) // 2;
            if nums[mid] == target:
                lastIndex = mid;
                low = mid + 1;
            elif nums[mid] < target:
                low = mid + 1;
            else:
                high = mid - 1;
        return lastIndex;


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstIndex = self.findFirstOccurence(nums, target);
        if firstIndex == -1:
            return [-1, -1];
        
        lastIndex = self.findSecondOccurence(nums, target);
        return [firstIndex, lastIndex];
        