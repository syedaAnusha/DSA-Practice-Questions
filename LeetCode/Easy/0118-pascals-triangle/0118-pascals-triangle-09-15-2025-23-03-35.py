class Solution(object):
    # Brute Force Approach
    # Time Complexity: O(n*n*r) => near about! => O(n^3)
    # Space Complexity: O(n) + O(n) => O(2n) = O(n) 

    def findnCr(self, n, r):
        res = 1;
        for i in range(r):
            res = res * (n-i);
            res = res // (i+1);
        return res;

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [];
        for r in range(1, numRows+1):
            templst = [];
            for c in range(1, r+1):
                templst.append(self.findnCr(r-1,c-1));
            ans.append(templst);
        return ans;
        