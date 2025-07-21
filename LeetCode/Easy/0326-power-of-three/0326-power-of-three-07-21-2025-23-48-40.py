import math;
class Solution(object):
    # Approach 2 - using simple log function
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False;
        else:
            ans = math.log(n) / math.log(3);
            if abs(ans - round(ans)) < 1e-9 and n % 3 == 0 or n == 1:
                return True;
            return False;
        