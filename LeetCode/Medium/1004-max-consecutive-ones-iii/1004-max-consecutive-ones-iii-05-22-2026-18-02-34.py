class Solution:
    # Optimal Approach - 01
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0;
        lenOfNums = len(nums);
        left = right = 0;
        zeroes = 0;
        while right < lenOfNums:
            if nums[right] == 0:
                zeroes += 1;
            if zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1;
                left += 1;
            maxLen = max(maxLen, right-left+1);
            right += 1;

        return maxLen;  