class Solution:
    # Brute Force Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i] <= k:
                k += 1;
            else:
                break;
        return k;
           