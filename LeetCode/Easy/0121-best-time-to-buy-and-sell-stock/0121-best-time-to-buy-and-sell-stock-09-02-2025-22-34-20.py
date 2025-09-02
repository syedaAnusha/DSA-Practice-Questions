class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0;
        MinBuy = prices[0];
        for i in range(1, len(prices)):
            sell = prices[i];
            cost = sell - MinBuy;
            maxProfit = max(maxProfit, cost);
            MinBuy = min(MinBuy, prices[i]);
        return maxProfit;