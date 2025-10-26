class Solution:
    # Optimal Approach
    # N = len(nums)
    # Time Complexity: O(N * log max(nums))
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
        n = len(nums);
        low = 1;
        high = max(nums);

        while low <= high:
            mid = (low+high) // 2;
            if self.getSum(nums, threshold, mid):
                high = mid - 1;
            else:
                low = mid + 1;
        return low;
        