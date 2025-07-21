class Solution(object):
    def findPowerOfFour(self, n, target, index):
        if n == 0 or target > n:
            return False;
        if target == n:
            return True;
        else:
            return self.findPowerOfFour(n, 1<<(2*index), index+1);

    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.findPowerOfFour(n, 1, 1);
        