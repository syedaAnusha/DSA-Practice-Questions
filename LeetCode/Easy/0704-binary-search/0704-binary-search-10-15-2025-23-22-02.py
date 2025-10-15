class Solution:
    # Optimal Approach - Recursive Solution
    # Time Complexity: O(log n)
    # Space Complexity: O(n) for calling function log n number of times
    def findTarget(self, arr, low, high, target):
        if low > high:
            return -1;
        else:
            mid = (low + high) // 2;
            if target == arr[mid]:
                return mid;
            elif target > arr[mid]:
                return self.findTarget(arr, mid+1, high, target);
            else:
                return self.findTarget(arr, low, mid-1, target);

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums);
        low = 0;
        high = n-1;   
        return self.findTarget(nums, low, high, target);
        
        


        