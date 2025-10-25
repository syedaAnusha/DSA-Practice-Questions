import math;
class Solution:
    def nthRoot(self, n, m):
       # code here
        ans = -1;
        for i in range(1,m+1):
            if math.pow(i, n) == m:
                return i;
            elif math.pow(i, n) > m:
                break;
        return ans;
