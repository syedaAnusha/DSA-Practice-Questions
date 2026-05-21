class Solution:
    # Optimal Approach
    # Time Complexity: O(2k)
    # Space Complexity: O(1)
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lSum = sum(cardPoints[0:k]);
        maxSum = lSum;
        rSum = 0;
        rightIndex = len(cardPoints)-1;
        for i in range(k-1, -1, -1):
            lSum -= cardPoints[i];
            rSum += cardPoints[rightIndex]; 
            Sum = lSum + rSum;
            maxSum = max(maxSum, Sum);
            rightIndex -= 1;   
        return maxSum;