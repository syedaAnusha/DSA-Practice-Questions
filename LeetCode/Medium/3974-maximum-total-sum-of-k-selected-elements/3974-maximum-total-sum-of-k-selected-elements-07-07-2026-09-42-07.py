class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        topKElementsList = nums[0:k]
        totalSum = 0
        curMul = mul
        for i in range(len(topKElementsList)):
            if curMul != 1:
                totalSum += (curMul)*topKElementsList[i]
                curMul -= 1
            else:
                totalSum += topKElementsList[i]
        return totalSum