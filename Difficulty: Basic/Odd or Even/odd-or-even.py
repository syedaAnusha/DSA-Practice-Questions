class Solution:
    def isEven (self, n):
        # code here
        if n & 1 == 1:
            return False;
        return True;