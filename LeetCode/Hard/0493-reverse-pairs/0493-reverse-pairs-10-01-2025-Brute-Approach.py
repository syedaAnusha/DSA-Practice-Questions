class Solution:
    # Brute Force Approach
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def reversePairs(self, nums: List[int]) -> int:
        pairCnt = 0;
        n = len(nums);
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > nums[j] * 2:
                    pairCnt += 1;
        return pairCnt;
