class Solution:
    # Optimal Approach
    # Time Complexity: O(log n) - In avg and best case, 
    # Time Complexity: O(n/2) In worst case
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums);
        low = 0;
        high = n - 1;

        while low <= high:
            mid = (low + high) // 2;
            if nums[mid] == target:
                return True;
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1;
                high -= 1;
                continue;

            if nums[mid] <= nums[high]:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1;
                else:
                    high = mid - 1;
            else:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1;
                else:
                    low = mid + 1;
        return False;

        
