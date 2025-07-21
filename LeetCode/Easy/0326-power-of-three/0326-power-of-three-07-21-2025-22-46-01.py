import math;
class Solution(object):
    def findPowerOfThree(self, target, n, index):
        if target == n:
            return True;
        if target > n or n <= 0:
            return False;
        else:
            return self.findPowerOfThree(math.pow(3, index), n, index+1);

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.findPowerOfThree(1, n, 1);
        