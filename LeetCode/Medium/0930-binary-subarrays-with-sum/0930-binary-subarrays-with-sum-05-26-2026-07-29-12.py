class Solution:
    # Optimal Approach
    # Time Complexity: O(2 * 2N)
    # Space Complexity: O(1)
    def findCountOfSubarrays(self, nums, goal):
        cntSubArrays = 0;
        lenOfNums = len(nums);
        left = right = 0;
        Sum = 0;
        if goal < 0:
            return 0;

        while right < lenOfNums:
            Sum += nums[right];
            while Sum > goal:
                Sum = Sum - nums[left];
                left += 1
            if Sum <= goal:
                cntSubArrays = cntSubArrays + (right-left+1);
            right += 1;
        return cntSubArrays;

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt1 = self.findCountOfSubarrays(nums, goal);
        cnt2 = self.findCountOfSubarrays(nums, goal-1);
        total = cnt1 - cnt2;
        return total;