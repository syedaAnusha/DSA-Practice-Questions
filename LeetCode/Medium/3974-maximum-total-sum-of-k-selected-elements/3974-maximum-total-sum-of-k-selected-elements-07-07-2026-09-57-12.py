import heapq
class Solution:
    # Optimal Approach
    # Time Complexity: O(N log k)
    # Space Complexity: O(k)
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        topKElements = heapq.nlargest(k, nums)
        totalSum = 0
        curMul = mul
        for num in topKElements:
            if curMul != 1:
                totalSum += (curMul)*num
                curMul -= 1
            else:
                totalSum += num
        return totalSum