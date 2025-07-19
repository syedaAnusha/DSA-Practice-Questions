class Solution(object):
    def findPowerOfTwo(self, n, index, target):
        if target > n or n == 0:
            return False;
        if target == n:
            return True;
        else:
            return self.findPowerOfTwo(n, index+1, 1<<index);
        
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        isPowerOfTwo = self.findPowerOfTwo(n, 0, 0);
        return isPowerOfTwo;
        