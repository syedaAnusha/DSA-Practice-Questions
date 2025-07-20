class Solution(object):
    def findLastRemaining(self, remain, step, head, left):
        if remain == 1:
            return head;
        if left or remain % 2 == 1:
            return self.findLastRemaining(remain // 2, step*2, head + step, not left);
        else:
            return self.findLastRemaining(remain // 2, step*2, head, not left);

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach 2 - using recursion
        lastElement = self.findLastRemaining(n, 1, 1, True);
        return lastElement;