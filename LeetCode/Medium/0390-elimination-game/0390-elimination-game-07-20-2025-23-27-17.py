class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach 1 - using loop
        head = 1;
        step = 1;
        remain = n;
        left = True;
        while remain > 1:
            if left or remain % 2 == 1:
                head += step;
            remain //= 2;
            step *= 2;
            left = not left; # change direction 
        return head;

        