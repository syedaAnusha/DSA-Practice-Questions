class Solution:
    # Brute Force Approach
    # N = len(nums)
    # Time Complexity: O(N * max(nums))
    # Space Complexity: O(1)
    def getSum(self, nums, threshold, divisor):
        Sum = 0;
        for i in range(len(nums)):
            res = (nums[i] + divisor - 1) // divisor; # equivalent of math.ceil for +ve nums for division.
            Sum += res;
            if Sum > threshold:
                return False;
        return True;
        
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maxNum = max(nums);
        for i in range(1, maxNum+1):
            if self.getSum(nums, threshold, i):
                return i;        
