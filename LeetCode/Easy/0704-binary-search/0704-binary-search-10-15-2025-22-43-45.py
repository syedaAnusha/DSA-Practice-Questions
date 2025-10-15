class Solution:
    # Optimal Approach - Iterative Solution
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums);
        low = 0;
        high = n-1;
        while low <= high:
            mid = (low + high) // 2;
            if target == nums[mid]:
                return mid;
            elif target > nums[mid]:
                low = mid+1;
            else:
                high = mid-1;
        return -1;
        
        


        